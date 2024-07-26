from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, world!")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello, world! this is about section")


def contact(request):
    return HttpResponse("Hello, world! this is contact secton")