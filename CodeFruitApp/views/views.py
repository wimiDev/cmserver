from django.http import JsonResponse
from rest_framework.views import APIView
from CodeFruitApp.models import User


class UserRegister(APIView):
    # 注册
    def get(self,request):
        get = request.GET
        username = get.get('username')
        password = get.get('password')
        
        users = User.objects.filter(UserName=username)
        data = {
            'status': 1,
            'message': 'account exist',
            }
        if len(users) <= 0:
           User.objects.create(UserName=username, UserPass=password)
           # 返回信息
           data = {
             'status':0,
             'message':'register success',
             'username':username,
             }
        return JsonResponse(data)

class UserLogin(APIView):
    def get(self,request):
        get = request.GET
        username = get.get('username')
        password = get.get('password')
        
        users = User.objects.filter(UserName=username)
        data = {
            'status': 1,
            'message': 'account not exist',
            }
        if len(users) > 0:
            user = users[0]
            if(user.UserPass == password):
                data = {
                    'status': 0,
                    'message': 'login sucess',
                    'username':username
                }

            else:
           # 返回信息
                data = {
                     'status':2,
                     'message':'account or passworld error',
                }
            

        return JsonResponse(data)
    

