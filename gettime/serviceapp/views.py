from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from datetime import datetime
import json
from django.views.decorators.http import require_http_methods


def showTime(request):
    response = {'datetime': datetime.now()}
    return JsonResponse(response)

# def getInfo(request):
#     data = json.loads(request.body)
#     id = data['id']
#     return JsonResponse({'age': datetime.now().year-id})