from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This will be the landing page!")
