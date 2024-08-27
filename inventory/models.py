from django.db import models
from django.utils import timezone

# Create your models here.

class Ingredient(models.Model):
  quantity = models.FloatField()
  unit = models.CharField(max_length=10)
  unit_price = models.FloatField()
  name = models.CharField(max_length=30)

class MenuItem(models.Model):
  price = models.FloatField()
  name = models.CharField(max_length=100)

class Purchase(models.Model):
  menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(default=timezone.now())

class RecipeRequirement(models.Model):
  menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
  quantity = models.FloatField()