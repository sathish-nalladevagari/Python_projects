from django.db import models

# Create your models here.


class Color(models.Model):
    color_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.color_name

class Person(models.Model):
    color = models.ForeignKey(Color, null= True, blank = True, on_delete=models.CASCADE, related_name='color')
    name = models.CharField(max_length=50)
    age = models.IntegerField()

