from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.First),
    path('fetch',views.fetch),
    path('show',views.show)
]