from django.db import models
from datetime import datetime

# Create your models here.

class Ingredient(models.Model):
  quantity = models.PositiveIntegerField()
  price = models.PositiveIntegerField()
  name = models.CharField(max_length=30)

class MenuItem(models.Model):
  price = models.PositiveIntegerField()
  name = models.CharField(max_length=100)
  ingredients = models.ManyToManyField(Ingredient, through=IngredientsOfMenuItem)

class Purchase(models.Model):
  time = models.DateTimeField(default=datetime.now())
  menu_items = models.ManyToManyField(MenuItem, through=PurchasedMenuItems)

class PurchasedMenuItems(models.Model):
  purchase = models.ForeignKey(Purchase)
  menu_item = models.ForeignKey(MenuItem)

class IngredientsOfMenuItem(models.Model):
  menu_item = models.ForeignKey(MenuItem)
  ingredient = models.ForeignKey(Ingredient)