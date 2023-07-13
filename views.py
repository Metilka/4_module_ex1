from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('This is my first website')

def les(request):
    return HttpResponse('Домашка по 4 занятию')
