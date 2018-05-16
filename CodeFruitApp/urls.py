from django.conf.urls import url, include
from CodeFruitApp import views

# api url 配置
urlpatterns = [
    url('test$', views.GetMessageView.as_view()),
]