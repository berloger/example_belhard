from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib import auth

def login(request):
    if not request.POST:
        return render(request, 'sign.html', csrf(request))
    else:
        user = auth.authenticate(password = request.POST['password'], username=request.POST['login'])
        if user:

            auth.login(request, user)
            return redirect('/')
        else:

            args = csrf(request)
            args['error'] = 'такого пользователя нет'
            return render(request, 'sign.html', args)


def logout(reuest):
    return HttpResponse('hello log')

def sign(request):
    return HttpResponse('hello log')
# Create your views here.
