from django.shortcuts import render

from .models import Adoption
from .serializers import AdoptionSerializer
from rest_framework import generics

class AdoptionListCreate(generics.ListCreateAPIView):
  queryset = Adoption.objects.all()
  serializer_class = AdoptionSerializer
