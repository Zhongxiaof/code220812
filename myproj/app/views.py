from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
import os
import uuid

# Create your views here.

def gotoIndex(request):
    return render(request,"index.html")

def getData(request):
    # 获取请求参数
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    print(num1+","+num2)
    # 处理业务逻辑
    # 返回响应
    return render(request,"index.html")

def gotoIndex2(request):
    return render(request,'index2.html')

# 定义一个接收GET请求的控制器函数
def getdata(request):
    # 接收客户端请求数据
    var = request.GET.get('params', 0)
    # 处理请求数据（终端输出）
    print('接收到客户端的GET请求参数数据: {0} 类型：{1}'.format(var, str(type(var))))
    # 响应客户端（在客户端浏览器输出参数值）
    return HttpResponse(var)

# 定义一个接收GET请求的加法控制器函数
def add(request):
    # 接收客户端请求数据
    var1 = int(request.GET.get('num1', 0))
    var2 = int(request.GET.get('num2', 0))
    # 处理请求数据（加法运算）
    result = var1 + var2
    # 响应客户端（在客户端浏览器输出参数值）
    return HttpResponse('结果为：{0}'.format(result))

# 定义一个接收RESTfule url规范的GET请求控制器函数
def bookInfo(request, bookname, year):
    # 处理请求数据
    bookname = '图书名称：《' + bookname + '》'
    year = '出版日期：' + str(year) + '年'
    # 响应客户端（在客户端浏览器输出参数值）
    return HttpResponse('{0}<br/>{1}'.format(bookname, year))

# 定义一个处理PSOT请求参数的控制器函数
def hello(request):
    # 判断请求类型（GET:页面跳转 POST:业务处理）
    if request.POST:
        # 接收客户端的请求参数
        name = request.POST.get('username', '')
        # 处理请求参数
        msg = '欢迎，{0}'.format(name) if name.lower() != 'monster' else '我不和怪物说话'
        # 响应客户端
        return HttpResponse(msg)
    else:
        # 响应客户端（页面跳转）
        return render(request, 'hello.html')

# 定义一个待参数的请求转发响应控制器函数
def search(request):
    # 判断请求类型（GET:页面跳转 POST:业务处理）
    if request.POST:
        # 接收客户端的请求参数
        keywords = request.POST.get('keywords', '')
        # 处理请求参数
        msg = '您搜索的关键字：{0}'.format(keywords)
        # 设置传递参数（字典类型）
        context = dict()
        context['message'] = msg
        # 响应客户端
        return render(request, 'search.html', context)
    else:
        # 响应客户端（页面跳转）
        return render(request, 'search.html')

