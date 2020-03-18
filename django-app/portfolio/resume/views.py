from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getExperience(request):
    return HttpResponse("Aditya has an experience of 4 years")