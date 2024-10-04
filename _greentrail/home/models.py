from django.db import models

# Create your models here.

class Signup(models.Model):
    
    forename = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    dob = models.DateField()
    
    
    
