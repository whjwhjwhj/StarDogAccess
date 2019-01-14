from SPARQLWrapper import SPARQLWrapper, BASIC
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
import json

def MeasurementData(request):
    if request.method == 'POST':
        print('weihaijun are in POST request')
        json_results =  HttpRequest.POST
        print(json_results)
        # datas = json.load(json_results)
        #
        # for data in datas:
        #     print(data)

        return HttpResponse(request)

