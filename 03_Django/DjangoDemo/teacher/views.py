from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.core.urlresolvers import reverse # 反向解析
from django.http import HttpResponseRedirect # 重定向
from django.shortcuts import render, render_to_response
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

def v10_1(r):
    return HttpResponseRedirect("/v11")

def v10_2(r):
    return HttpResponseRedirect(reverse("v11"))

def v11(r):
    return HttpResponse("这是v11的访问返回内容")

def v8_get(r):
    rst = ""
    for k,v in r.GET.items():
        rst += k + "----->" + v
        rst += ","
    return HttpResponse("get value of GET is {0}".format(rst))

def v9_get(r):
    return render_to_response("for_post.html")

def v9_post(r):
    rst = ""
    for k,v in r.POST.items():
        rst += k + "----->" + v
        rst += ","
    return HttpResponse("get value of POST is {0}".format(rst))
