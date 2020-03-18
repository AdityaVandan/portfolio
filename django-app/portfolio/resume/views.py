from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getExperience(request):
    return render(request,"abc.html")
