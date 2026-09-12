from django.db import models
class student(models.Model):
    name =models.CharField(max_length=30)
    age=models.ImageField()
    city =models.CharField(max_length=50)
    def __str__(self):
        return self.name
# Create your models here.
