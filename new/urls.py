from django import urls
from django.urls import path
from new import views

urlpatterns = [
    path('',views.index),
    path('<str:name>/',views.greet)
]