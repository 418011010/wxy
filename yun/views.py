from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def hello(request):
    return JsonResponse({'result': 200, 'msg': '连接成功'})