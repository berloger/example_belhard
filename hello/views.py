from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Videos, Comment
from django.template.context_processors import csrf
from django.contrib.auth.models import User


def hello(request):
    return render(request, 'allvideo.html', {'videos':Videos.objects.all(), 'comments':Comment.objects.all(), 'user':request.user})


def login(request):
    if request.GET:
        print('GET')
        print(request.GET['login'])
        print(request.GET['password'])
        return redirect('/hello/login/')
    elif request.POST:
        print('POST')
        print(request.POST['login'])
        print(request.POST['password'])
        return redirect('/hello/login/')
    else:
        return render(request, 'index.html', csrf(request))


def addvideo(request):
    if request.GET:
        newvideo = Videos()
        newvideo.video_name = request.GET['name']
        newvideo.video_url = request.GET['url']
        newvideo.save()
    return redirect('/')


def addcomment(request, video_id):
    if request.GET:
        newcom = Comment()
        newcom.comment_text = request.GET['comment']
        newcom.comment_video_id = video_id
        #newcom.comment_user = User.objects.get(id=request.user.id)
        newcom.comment_user_id = request.user.id
        newcom.save()
    return redirect('/')

def onevideo(request, video_id):
    video = Videos.objects.get(id=video_id)
    comments = Comment.objects.filter(comment_video_id = video_id)
    return render(request, 'onevideo.html', {'video':video, 'comments':comments})