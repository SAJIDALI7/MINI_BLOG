from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, UserLoginForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Post
from django.core.cache import cache
from django.core.paginator import Paginator
# from miniblogapp import signals
# Create your views here.
def home(request):
    # signals.notification.send(sender=None, request=request, user=['Sajid', 'Charawala'])
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'posts': page_obj})

def signup_page(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!!, you have been successfully Author.')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignupForm()
    return render(request, 'signuppage.html', {'form': form})


def login_page(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserLoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'you have been successfully logged in')
                    return HttpResponseRedirect('/miniblog/dashboard/')
        else:
            form = UserLoginForm()
        return render(request, 'loginpage.html', {'form': form})
    else:
        return HttpResponseRedirect('/miniblog/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('ip', 0)
        ct = cache.get('count', version=user.pk)

        return render(request, 'dashboard.html', {'posts': posts, 'full_name': full_name, 'groups': gps, 'ip': ip, 'ct': ct})
    else:
        return HttpResponseRedirect('/miniblog/loginpage/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title, desc=desc)
                messages.info(request,'Your post successfully Added!!')
                pst.save()
                return HttpResponseRedirect('/miniblog/dashboard/')
        else:
            form = PostForm()
        return render(request, 'addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/miniblog/loginpage/')


def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, f'{request.user} {id} successfully UPDATE')
                return HttpResponseRedirect('/miniblog/dashboard/')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/miniblog/loginpage/')


def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            pi.delete()
            messages.warning(request,f'{request.user} {id} Post DELETED')
        return HttpResponseRedirect('/miniblog/dashboard/')
    else:
        return HttpResponseRedirect('/miniblog/loginpage/')