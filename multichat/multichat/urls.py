# from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from chat.views import index


# urlpatterns = [
#     path('', index),
#     path('accounts/login/', login),
#     path('accounts/logout/', logout),
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    url(r'^$', index),
    url('accounts/login/', login),
    url('accounts/logout/', logout),
    url('admin/', admin.site.urls),
]
