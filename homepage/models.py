from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    newFeatures = models.TextField(null=True)
    serviceImageUrl = models.FileField()

    def __str__(self):
      return self.name


class Plan(models.Model):
    Planname = models.CharField(max_length=100)
    Plandescription = models.TextField()
    previous_price = models.IntegerField(null = True)
    current_price = models.IntegerField()
    service = models.ForeignKey(Service, null = True , on_delete=models.SET_NULL)

    def __str__(self):
        return self.Planname

