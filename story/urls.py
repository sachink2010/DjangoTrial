from django.urls import path
from . import views

urlpatterns = [
    path('intro/', views.intro),
    path('story/', views.story),
    path('code/', views.code),
    path('', views.intro),
]