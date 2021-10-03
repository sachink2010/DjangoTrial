from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('story/', views.story),
    path('', views.say_hello),
]