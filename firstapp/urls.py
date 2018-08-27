from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LoginFormView.as_view(),name="index"),
    path('about/', views.about ,name="about"),
    path('book/', views.book ,name="book"),
    path('home/', views.home, name="home"),

    path('register/', views.RegisterFormView.as_view(), name='signup'),
    #path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.logoutForm, name='logout'),

]



