# import datetime
# import hashlib
#
# from django.views import View
#
#
# from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
# import re
# import json
from login import models
# from django.db.models import Q
from rest_framework.response import Response
# from django.conf import settings
# import os

class Showallwine(APIView):
    def get(self,request):
        allwine=models.Wine.objects.all()
        l=[]
        for i in allwine:
            l.append({'name':i.name,'price':i.price,'img_url':i.img_url})
        return Response(data={"res": l})





# class OrderPayView(APIView):
#     def post(self,request):
#         #判断用户是否登录
#         user = request.data['user']
#
#         #接收参数
#         order_id = request.data.get('order_id')
#         #校验参数
#         if not order_id:
#             return Response(data={"res":'1',"errmsg":"无效的订单id"})
#         try:
#             #order_id:订单id，user：用户，pay_method=3:支付方式(支付宝),order_status:订单状态(未支付)
#             order = OrderInfo.objects.get(pay_method='3')
#         except Exception:
#             return Response(data={"res":'2',"errmsg":"订单错误"})
#         #业务处理:使用Python sdk调用支付宝的支付接口
#         alipay = AliPay(
#             appid="2019112769454407",   #APPID
#             app_notify_url=None,  # 默认回调url,可以传也可以不传
#             app_private_key_path=os.path.join(settings.BASE_DIR,"apps\\order\\app_private_key.pem"), #私钥的路径
#             alipay_public_key_path=os.path.join(settings.BASE_DIR,"apps\\order\\app_public_key.pem"),#支付宝公钥的路径
#             sign_type="RSA2",  # RSA 或者 RSA2，签名的算法
#             debug = False  # 默认False，沙箱环境改成True
#         )
#         #借助alipay对象，向支付宝发起支付请求
#         #电脑网站支付，需要跳转到https://openapi.alipaydev.com/gateway.do?+order_string
#         total_pay = order.price #订单总金额
#         order_string = alipay.api_alipay_trade_page_pay(
#             out_trade_no=order_id,  #订单id
#             total_amount=str(total_pay), #支付宝总金额
#             subject="卢本伟牛逼%s"%order_id, #订单标题
#             return_url=None,
#             notify_url=None,
#
#         )
#         #返回应答
#         pay_url = "https://openapi.alipay.com/gateway.do?"+order_string
#         return Response(data={"res":'3',"pay_url":pay_url})