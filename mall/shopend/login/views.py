import datetime
import hashlib

from django.views import View

from .serializer import *
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
import re
import json
from .models import *
from django.db.models import Q
from rest_framework.response import Response
from alipay import AliPay
from django.conf import settings
import os


class LoginView(APIView):
    def post(self,request):
        author = request.data['phone']
        print(author)
        # print(Author.objects.filter(username=author))
        # if Author.objects.filter(username=author):
        #     return Response(data={"msg":'用户已存在'})
        # authors = AuthorModelSerializers(data=request.data)
        # if authors.is_valid():
        #     authors.save()
        #     return Response(authors.data)
        return Response(data={'asdf':'adfsa'})


class RelLoginView(APIView):
    def get(self,request):
        user = request.GET.get("username")
        pw = request.GET.get("pw")
        print(user)
        old_user = Author.objects.filter(username=user)
        if not old_user:
            return Response(data={"msg": '无该用户'})
        psd=Author.objects.filter(pw=pw)
        if not psd:
            return Response(data={"msg": '密码不一致'})
        Authors = AuthorModelSerializers(old_user, many=True)
        return Response(Authors.data)


class BlogView(APIView):
    def get(self, request):
        author = request.GET.get("author")
        blog_list = bloginfo.objects.filter(lable='public')
        blogs = bloginfoModelSerializers(blog_list, many=True)
        return Response(blogs.data)
    def post(self, request):
        blogs = bloginfoModelSerializers(data=request.data)
        if blogs.is_valid():
            blogs.save()
            return Response(blogs.data)
        return Response(blogs.errors)
    def delete(self,request):
        id = request.GET.get("id")
        bloginfo.objects.filter(id=id).delete()
        return Response()

    def put(self, request):
        pk=request.data['id']
        content=request.data['content']
        title=request.data['title']
        blog_obj = bloginfo.objects.filter(id=pk).first()
        blog_obj.title = title
        blog_obj.content=content
        blog_obj.save()
        return Response(data={"msg": '修改成功'})


class BlogView2(APIView):
    def get(self, request):
        author = request.GET.get("author")
        print(author)
        blog_list = bloginfo.objects.filter(Q(lable='private') & Q(author=author))
        blogs = bloginfoModelSerializers(blog_list, many=True)
        return Response(blogs.data)
    def delete(self,request):
        title = request.GET.get("title")
        bloginfo.objects.filter(title=title).delete()
        return Response()

class OrderPayView(APIView):
    def post(self,request):
        #判断用户是否登录
        user = request.data['user']

        #接收参数
        order_id = request.data.get('order_id')
        #校验参数
        if not order_id:
            return Response(data={"res":'1',"errmsg":"无效的订单id"})
        try:
            #order_id:订单id，user：用户，pay_method=3:支付方式(支付宝),order_status:订单状态(未支付)
            order = OrderInfo.objects.get(order_id=order_id,user=user,pay_method='3',order_status='1')
        except Exception:
            return Response(data={"res":'2',"errmsg":"订单错误"})
        #业务处理:使用Python sdk调用支付宝的支付接口
        alipay = AliPay(
            appid="2019112769454407",   #APPID
            app_notify_url=None,  # 默认回调url,可以传也可以不传
            app_private_key_path=os.path.join(settings.BASE_DIR,"apps\\order\\app_private_key.pem"), #私钥的路径
            alipay_public_key_path=os.path.join(settings.BASE_DIR,"apps\\order\\app_public_key.pem"),#支付宝公钥的路径
            sign_type="RSA2",  # RSA 或者 RSA2，签名的算法
            debug = False  # 默认False，沙箱环境改成True
        )
        #借助alipay对象，向支付宝发起支付请求
        #电脑网站支付，需要跳转到https://openapi.alipaydev.com/gateway.do?+order_string
        total_pay = order.price #订单总金额
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id,  #订单id
            total_amount=str(total_pay), #支付宝总金额
            subject="卢本伟牛逼%s"%order_id, #订单标题
            return_url=None,
            notify_url=None,

        )
        #返回应答
        pay_url = "https://openapi.alipay.com/gateway.do?"+order_string
        return Response(data={"res":'3',"pay_url":pay_url})