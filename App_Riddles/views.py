from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def riddles(request):
    return HttpResponse('Hello RIDDLES')