from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
