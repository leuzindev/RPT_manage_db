from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.FloatField(max_length=100, null=False)
    description = models.TextField()

    def __str__(self):
        return self.name
        
