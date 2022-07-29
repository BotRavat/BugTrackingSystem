 

from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('signup',views.signup,name='singup'),
    path('handlelogin',views.handlelogin,name='handlelogin'),
    path('handlelogout',views.handlelogout,name='handlelogout')

    
]