from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveBigIntegerField()

    def __str__(self):
            return self.name
    
class Product(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name