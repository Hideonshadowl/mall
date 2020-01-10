from django.contrib import admin
from django.urls import path
from login import views


urlpatterns = [
    path(r'showallwine/', views.Showallwine.as_view()),
    # path(r'pay/',views.OrderPayView.as_view(),name="pay"),
]