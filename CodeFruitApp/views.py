from django.http import JsonResponse
from rest_framework.views import APIView
from CodeFruitApp.models import User


class UserRegister(APIView):
    # 注册
    def get(self,request):
        get = request.GET
        username = get.get('username')
        password = get.get('password')

        User.objects.get(UserName=username)
        User.objects.create(UserName="12344", UserPass="21312")

        # 返回信息
        data = {
            'status': 1,
            'message': 'success',
            'username': username,
            'password': password,
        }
        return JsonResponse(data)