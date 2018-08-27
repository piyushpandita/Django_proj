from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
class bigb(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title




class Item(models.Model):
    """docstring for Item"""
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=1,
                                validators=[MaxValueValidator(1000), MinValueValidator(1)])
    qty = models.IntegerField(default=1,
                              validators=[MaxValueValidator(10), MinValueValidator(1)])






