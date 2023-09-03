from django.db import models


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=240)
    price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name}- {self.price}"