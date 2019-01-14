"""定义StarDog的URL模式"""
from django.urls import path
from . import views
urlpatterns = [
    # 主页
   path('', views.MeasurementData, name='MeasurementData'),
]