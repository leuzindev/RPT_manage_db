from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=150, null=False)
    password = models.CharField(max_length=150, null=False)
    
    def __str__(self):
        return self.name
        
