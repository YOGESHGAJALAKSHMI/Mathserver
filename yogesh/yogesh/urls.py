from django.contrib import admin
from django.urls import path
from rateapp import views


urlpatterns = [path('', views.calculate_rate, name='calculate_rate'),]