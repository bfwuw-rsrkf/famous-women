from django.db import models


class Product(models.Model):
    model = models.CharField(max_length=256)
    price = models.FloatField(default=0)
    color = models.CharField(max_length=256)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.model


class Woman(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    job = models.CharField(max_length=256)
    salary = models.FloatField(default=0)

    def __str__(self):
        return self.name
