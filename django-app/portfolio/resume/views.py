from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from resume.info import person
# Create your views here.


def getExperience(request):
    return render(request,"abc.html")

def getInfo(request):
    return JsonResponse(person)
