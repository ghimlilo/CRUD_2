from django.db import models
from django.db.models.deletion import CASCADE

class Person(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length =128)
    age = models.IntegerField(default=0)


    class Meta: 
        db_table = 'persons'


class Dog(models.Model):
    # name = models.CharField(max_length = 20)
    # age  = models.IntegerField(default=0)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    class Meta:
        db_table = 'dogs'

# Create your models here.
 