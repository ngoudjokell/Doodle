from django.db import models
from django import forms

# Create your models here.
class Etudiants(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/', blank = True, null =True)


    




   
