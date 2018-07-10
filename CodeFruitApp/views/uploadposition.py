from django.http import JsonResponse
from rest_framework.views import APIView
from CodeFruitApp.models import User
from CodeFruitApp.models import UserPosition

class UpLoadPosition(APIView):
	#
	def get(self,request):

		getComponent = request.GET
		username = getComponent.get('username')
		token = getComponent.get('token')
		longitude = getComponent.get('longitude')
		latitude = getComponent.get('latitude')

		response = {
			'status':0,
			'message':'success',
		}

		if(len(token) <= 0):
			response = {
				'status':1,
				'message':'not login',
			}

		users = User.objects.filter(UserName=username)
		if(len(users) <= 0):
			response = {
				'status':2,
				'message':'user not exist',
			}
		userToken = users[0].Token

		if(userToken != token):
			response = {
				'status':3,
				'message':'token failure',
			}

		UserPosition.objects.create(UserName = username, longitude = longitude, latitude = latitude, uploaddate = '2136478234')
		return JsonResponse(response)


#http://127.0.0.1:8000/CodeFruit/position?username=cyy&token=123456&longitude=11.34&latitude=11.35