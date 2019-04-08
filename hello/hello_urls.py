from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.hello),
    path('login/', views.login),
    path('addvideo/', views.addvideo),
    re_path('^addcomment/(?P<video_id>\d+)/$', views.addcomment),
    re_path('^onevideo/(?P<video_id>\d+)/$', views.onevideo),
]