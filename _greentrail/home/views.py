from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(request):
    return HttpResponse("This will be the landing page!")

@api_view(['GET'])
def api_test(request):
    data = {
        "message": "API is working!",  # Just a simple test message
    }
    return Response(data)
