from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('cinemafinder/', views.cinemafinder, name='blog-cf'),
    path('latest/', views.latest, name='latest'),
    path('announcements/', views.announcements, name='announcements'),
    path('calendars/', views.calendars, name='calendars')
]