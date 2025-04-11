from django.contrib import admin
from django.urls import path

from app import views
from app.views import index
urlpatterns = [
    path('', views.index),
]
