from django.contrib import admin
from django.urls import path, include
from .views import AnimalCreateView, AnimalDetailView, AnimalAllView, UserAllView

urlpatterns = [
    path('create/', AnimalCreateView.as_view()),
    path('detail/<int:pk>', AnimalDetailView.as_view()),
    path('getAll/', AnimalAllView.as_view()),
    path('users/', UserAllView.as_view())
]
