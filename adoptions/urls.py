from django.urls import path
from . import views

urlpatterns = [
    path('api/adoption/', views.AdoptionListCreate.as_view() ),
]