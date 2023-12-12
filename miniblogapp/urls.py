from django.urls import path, include
from . import views
urlpatterns = [
    path('signuppage/', views.signup_page, name='signuppage'),
    path('loginpage/', views.login_page, name='loginpage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logoutpage/', views.user_logout, name='logoutpage'),
    path('addpost/', views.add_post, name='addpost'),
    path('updatepost/<int:id>/', views.update_post, name='updatepost'),
    path('deletepost/<int:id>', views.delete_post, name='deletepost'),
]
