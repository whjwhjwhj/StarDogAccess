from SPARQLWrapper import SPARQLWrapper, BASIC
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import json

def MeasurementData(request):
    if request.method == 'POST':
        print('weihaijun are in POST request')

        datas = json.loads(HttpRequest.body)

        for key,value in datas.items():
            print(key,value)

        return HttpResponse(request)

