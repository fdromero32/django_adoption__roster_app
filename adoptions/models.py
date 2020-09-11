from django.db import models

class Adoption(models.Model):
  SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]

  name = models.CharField(max_length=100)
  species = models.CharField(max_length=30)
  breed = models.CharField(max_length=30, blank=True)
  description = models.TextField(blank=True)
  sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
  age = models.IntegerField(null=True)
  submitter = models.CharField(max_length=100)
  submission_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True) 
