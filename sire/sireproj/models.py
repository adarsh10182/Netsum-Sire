from pyexpat import model
from turtle import mode
from django.db import models

# Create your models here.
class VesselDisc(models.Model):
    Vtype=models.CharField(max_length=100)
    PDesc=models.CharField(max_length=200)

class Question(models.Model):
    Chapter=models.CharField(max_length=3)
    Stext=models.CharField(max_length=100)
    Ftext=models.CharField(max_length=400)
    Qno=models.CharField(max_length=10)
    HQtn=models.CharField(max_length=30)
    PQtn=models.CharField(max_length=30)
    HuQtn=models.CharField(max_length=30)
    Qtype=models.CharField(max_length=10)
    Chemical=models.BooleanField()
    LNG=models.BooleanField()
    LPG=models.BooleanField()
    Oil=models.BooleanField()
    Conditional=models.BooleanField()
    Roviq=models.CharField(max_length=300)
    Rovset=set