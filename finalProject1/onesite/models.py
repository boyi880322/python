from django.db import models

# Create your models here.
class zone(models.Model):
    code = models.CharField(max_length=5,null=True)
    city = models.CharField(max_length=10)
    count = models.PositiveIntegerField()
    
    def __str__(self):
        return self.city

class foreign(models.Model):
    country = models.CharField(max_length=10)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.country

class monthcase(models.Model):
    month = models.PositiveIntegerField()
    count = models.PositiveIntegerField()


class weekcase(models.Model):
    week = models.PositiveIntegerField()
    count = models.PositiveIntegerField()

class info(models.Model):
    year = models.PositiveIntegerField()
    week = models.PositiveIntegerField()
    city = models.CharField(max_length=3)
    gender = models.CharField(max_length=1)
    imported = models.CharField(max_length=1)
    age = models.CharField(max_length=10)
    count = models.PositiveIntegerField()        