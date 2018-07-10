from django.conf.urls import url, include
from CodeFruitApp.views import uploadposition
from CodeFruitApp.views import login_and_register

# api url 配置
urlpatterns = [
    url('register/$', login_and_register.UserRegister.as_view()),
    url('login/$', login_and_register.UserLogin.as_view()),
    url('position/$', uploadposition.UpLoadPosition.as_view()),
]
