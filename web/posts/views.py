from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.


def hello_api(request):
    return JsonResponse({"Result": "Hello world new data testing"})

