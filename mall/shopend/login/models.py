from django.db import models
from .myvalidators import *


class OrderInfo(models.Model):
    order_id = models.CharField(unique=True, max_length=22)
    user = models.CharField(max_length=100)
    pay_method = models.CharField(max_length=100)
    order_status = models.CharField(max_length=100)
    price=models.IntegerField(max_length=100)

class Wine(models.Model):
    name = models.CharField(unique=True, max_length=100)
    volume = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    is_in_home=models.CharField(max_length=100)
    category=models.CharField(max_length=100)