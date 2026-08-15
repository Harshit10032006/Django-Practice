from django.db import models

# Create your models here.


class Color(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE,null=True, blank=True, related_name='people') # person_set.all() -> perple.all() 
    
    def __str__(self):
        return self.name