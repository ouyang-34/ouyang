"""为应用程序users定义URL模型"""

from django.urls import path,include
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout,login,authenticate
from . import views
app_name = 'users'
LoginView.template_name = 'users/login.html'
urlpatterns = [
    #登录页面
    path('login/',LoginView.as_view(),name='login'),
    #注销
    path('logout/',views.logout_view,name='logout'),
    #注册
    path('register/',views.register,name='register'),
    ]
