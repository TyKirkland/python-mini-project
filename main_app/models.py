from django.db import models

# Create your models here.
    
class Species(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250, default='')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
    
class Cephalopod(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name="cephalopods")

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name="animal")

    def __str__(self):
        return self.name
