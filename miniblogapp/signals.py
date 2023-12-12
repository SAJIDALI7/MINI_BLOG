from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.dispatch import Signal, receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_migrate, post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created
from django.core.cache import cache

# @receiver(user_logged_in, sender=User)
# def login_success(sender, request, user, **kwargs):
#     print("-------------------------------------"
#           "----------------------------------------")
#     print("sender:", sender)
#     print("username:", user)
#     print("user password:", user.password)
#     print("Request:", request)
#     print(f"kwargs: {kwargs}")
#
# @receiver(post_save,sender=User)
# def at_endign_save(sender, instance, created, **kwargs):
#     print("---------------------------------------"
#           "---------------------------------------")
#     print('sender', sender)
#     print('created', created)
#     print('instance', instance)
#     print(f'kwargs: {kwargs}')

# @receiver(request_started)
# def at_beginnig_request(sender,environ, **kwargs):
#     print("======================================"
#           "======================================")
#     print("sender", sender)
#     print("Environ:", environ)
#     print(f"kwargs: {kwargs}")

# @receiver(pre_migrate)
# def before_install_apps(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
#     print("start====================================="
#           "======================================")
#     print("sender", sender)
#     print("app_config", app_config)
#     print("verbosity", verbosity)
#     print("interactive", interactive)
#     print("using", using)
#     print("plan", plan)
#     print("apps", apps)
#     print(f"kwargs: {kwargs}")
#
#
# @receiver(post_migrate)
# def after_install_apps(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
#     print("end======================================"
#           "======================================")
#     print("sender", sender)
#     print("app_config", app_config)
#     print("verbosity", verbosity)
#     print("interactive", interactive)
#     print("using", using)
#     print("plan", plan)
#     print("apps", apps)
#     print(f"kwargs: {kwargs}")


# @receiver(connection_created)
# def db_created(sender, connection, **kwargs):
#     print("========================================"
#           "========================================")
#     print('sender', sender)
#     print('connection', connection)
#     print(f"kwargs: {kwargs}")

# @receiver(user_logged_in, sender=User)
# def db_created(sender, request, user, **kwargs):
#     ip = request.META.get("REMOTE_ADDR")
#     request.session['ip'] = ip
#
# @receiver(user_logged_in, sender=User)
# def db_created(sender, request, user, **kwargs):
#     ct = cache.get('count', 0, version=user.pk)
#     newct = ct + 1
#     cache.set('count', newct, 60*60*24,version=user.pk)
#     print(user.pk)


# notification = Signal(providing_args=["request", "user"])
#
# @receiver(notification)
# def show_notification(sender, **kwargs):
#     print(sender)
#     print(f'{kwargs}')
#     print("Notification")