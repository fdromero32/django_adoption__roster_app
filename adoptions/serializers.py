from rest_framework import serializers
from .models import Adoption

class AdoptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Adoption
    fields = ('id', 'name', 'species', 'breed', 'description', 'sex', 'age', 'submitter', 'submission_date')