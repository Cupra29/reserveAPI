from django.db import models

# Create your models here.

class Reserve(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name