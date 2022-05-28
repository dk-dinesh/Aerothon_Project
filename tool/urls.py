from django.contrib import admin
from django.urls import path, include
from tool import views



urlpatterns = [
    path('',views.home,name='home'),
    path('tool/',views.Tool,name='tool'),
    path('team/',views.Team,name='team'),
    path('download/',views.Download,name='download'),
    path('generate/',views.Generate,name='generate')
]
