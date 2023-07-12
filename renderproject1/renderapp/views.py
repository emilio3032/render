from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("first page")


def about(request):
    return render(request,"about.html")


def contact(request):
    return HttpResponse("third page")
def details(request):
    return render(request,"details.html")
def thanks(request):
    return HttpResponse("lastpage")


