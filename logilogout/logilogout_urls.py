from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('out/', views.logout),
    path('sign/', views.sign),
]