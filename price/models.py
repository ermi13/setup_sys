from django.db import models

# Create your models here.
class Discount(models.Model):
    description = models.CharField(max_length=1000)
    days = models.IntegerField()
    hours = models.IntegerField()
    minutes = models.IntegerField()
    seconds = models.IntegerField()

    def __str__(self):
        return self.description
