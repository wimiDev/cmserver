from django.http import JsonResponse
from rest_framework.views import APIView
from CodeFruitApp.models import User

# 注册
class UserRegister(APIView):
    def get(self,request):
        get = request.GET
        username = get.get('username')
        password = get.get('password')

        users = User.objects.filter(UserName=username)
        data = {}
        if(users):
            data = {
            'status': 1,
            'message': 'account exist',
            'username': username,
            }
        else:
            User.objects.create(UserName=username, UserPass=password)

            # 返回信息
            data = {
                'status': 0,
                'message': 'success',
                'username': username,
            }
        return JsonResponse(data)

class UserLogin(APIView):

    def get(self,request):
        get = request.GET
        username = get.get('username')
        password = get.get('password')
        users = User.objects.filter(UserName=username)
        data = {
                'status': 3,
                'message': 'account not exist',
            }
        
        if(len(users)>0):
            user = users[0]
            if(password != user.UserPass):
                data = {
                    'status': 2,
                    'message': 'username or password error',
                    'username': username,
                }
            else :
                data = {
                    'status': 0,
                    'message': 'hello, you are my world',
                    'username': username,
                }

        return JsonResponse(data)
           

