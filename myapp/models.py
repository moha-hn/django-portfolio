from django.db import models

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(blank=True)
    phone=models.IntegerField()
    message=models.TextField(blank=True)
    def __str__(self):
        return self.name