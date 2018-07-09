from django.conf.urls import url, include
from CodeFruitApp import views

# api url 配置
urlpatterns = [
    url('register/$', views.UserRegister.as_view()),
    url('login/$', views.UserLogin.as_view()),
]
