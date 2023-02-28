from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=300)


    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length="300")
    age = models.PositiveIntegerField()
    birthday = models.DateField()