from django.shortcuts import render
from django.http import JsonResponse
import requests, json,re
# Create your views here.


def hello(request):
    return JsonResponse({'result': 200, 'msg': '连接成功'})


def test(request):
    url = 'http://ip.ws.126.net/ipquery?ip=104.28.10.90'
    r = requests.get(url,)
    #out = re.findall('localAddress={city:"荆门市", province:"湖北省"}',r.text)
    out = re.findall('province:"(.*?)"', r.text)
    # print(out)

    pr = {}
    pr.update(province=out[0])

    return JsonResponse(pr)

