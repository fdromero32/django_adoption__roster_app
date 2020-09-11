from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('adoptions.urls')),
    path('', include('frontend.urls')),
]
