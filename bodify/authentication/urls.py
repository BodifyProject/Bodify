from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.auth, name='auth'),
    path('loginAuth/', views.loginAuth, name='loginAuth'),

]
