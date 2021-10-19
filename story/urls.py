from django.urls import path
from . import views

urlpatterns = [
    path('intro/', views.intro),
    path('story/', views.story),
    path('', views.intro),
]