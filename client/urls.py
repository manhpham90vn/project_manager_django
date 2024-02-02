from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new),
    path('show/<int:id>', views.show),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
