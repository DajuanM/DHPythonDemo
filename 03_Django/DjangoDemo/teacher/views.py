from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.core.urlresolvers import reverse
# Create your views here.

# 视图函数需要有一个参数，类型是HttpResponse
def do_normalmap(request):
    # 此时student是一个dict格式内容，不是json
    student = {
        "name": "luidana",
        "age": 18,
        "mobile": "15578875040"
    }
    return JsonResponse(student)
    # return HttpResponse("this is normalmap")

def withparams(request, year, month):
    return HttpResponse("{0}-{1}".format(year, month))

def do_app(r):
    return HttpResponse("这是一个子路由")
# 参数名跟路由里参数名要一样
def do_param2(r, pn):
    return HttpResponse('这是第{0}页'.format(pn))

def extremParam(r, name):
    return HttpResponse('My name is {0}'.format(name))

def revParse(r):
    return HttpResponse("Your request url is {0}".format(reverse("askname")))

def v_exception(r):
    raise Http404
    return HttpResponse("OK")