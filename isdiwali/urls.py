from django.urls import path 
from isdiwali import views

urlpatterns = [
    path('',views.index)
]