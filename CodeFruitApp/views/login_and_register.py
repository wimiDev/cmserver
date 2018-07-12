from django.http import JsonResponse
from rest_framework.views import APIView
from CodeFruitApp.models import User
from CodeFruitApp.tool import tokentool
import time


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
        usertoken = get.get('token')
        
        users = User.objects.filter(UserName=username)
        data = {
            'status': 1,
            'message': 'account not exist',
            }
        if len(users) > 0:
            user = users[0]
            stmp = time.time()
            extren = int(round(stmp * 1000))
            if(user.UserPass == password):
                #creat token
                tokenMaker = tokentool.TokenMaker()
                token = tokenMaker.createToken(str(extren))
                user.Token = token
                user.LoginState = User.ONLINE
                user.LoginTime = str(extren)
                data = {
                    'status': 0,
                    'message': 'login sucess',
                    'username':username,
                    'token':user.Token,
                }
                user.save()
            elif(user.Token == usertoken):
                user.LoginState = User.ONLINE
                user.LoginTime = str(extren)
                data = {
                    'status': 0,
                    'message': 'login sucess',
                    'username':username,
                }
                user.save()
            else:
           # 返回信息
                data = {
                     'status':2,
                     'message':'account or passworld error',
                }
            

        return JsonResponse(data)
    
    #http://127.0.0.1:8000/CodeFruit/login/?username=cyy&password=123456
    #http://127.0.0.1:8000/CodeFruit/login/?username=cyy&token=0fe44f77d572b251671795017b7e97b2ef589ccf

