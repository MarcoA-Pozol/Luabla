from django.shortcuts import render, HttpResponse

def listening(request):
    return HttpResponse('Hello LISTENING')