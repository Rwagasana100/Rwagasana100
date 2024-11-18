from django.db import models

# Create your models here.
class Customers(models.Model):
  names=models.CharField( max_length=50)
  address=models.CharField(max_length=70)
  age=models.PositiveIntegerField(max_length=12)
  def __str__(self):
    return f"{self.names}"
class Enterepreneur(models.Model):
  company=models.CharField(max_length=123)
  age=models.PositiveIntegerField()
  location=models.CharField(max_length=132)
  def __str__(self):
    return f"{self.company}"