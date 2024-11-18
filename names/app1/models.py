from django.db import models

# Create your models here.
class Students(models.Model):
  first_name=models.CharField(max_length=222)
  last_name=models.CharField(max_length=233)
  age=models.PositiveIntegerField(null=False)
  
  def __str__(self):
    return f"{self.first_name} {self.last_name}"
  
class Staff(models.Model):
  email=models.EmailField()
  address=models.CharField(max_length=121)
  nationality=models.CharField(max_length=124)
  
  def __str__(self):
    return self.email
  
