import datetime

from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView


class GetMessageView(APIView):
    # get 请求
    def get(self, request):
        # 获取参数数据
        get = request.GET
        # 获取参数 a
        a = get.get('a')
        # 返回信息
        d = {
            'status': 1,
            'message': 'success',
            'params' : a,
            }
        return JsonResponse(d)