from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    address=models.TextField()

    def __str__(self):   
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()    
    age = models.IntegerField()
    orderdate=models.DateField(auto_now_add=True)


    def __str__(self):   
        return str(self.age)