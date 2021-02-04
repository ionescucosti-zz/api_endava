from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('pow', views.power),
    path('fib', views.fib),
    path('fact', views.fact),
]