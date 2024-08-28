from django import form_class
from .models import *

class PurchaseForm(models.ModelForm):
  class Meta:
    model = Purchase
    fields = "__all__"

class MenuItemForm(models.ModelForm):
  class Meta:
    model = MenuItem
    fields = "__all__"

class RecipeRequirementForm(models.ModelForm):
  class Meta:
    model = RecipeRequirement
    fields = ("ingredient", "quantity")

class IngredientForm(models.ModelForm):
  class Meta:
    model = Ingredient
    fields = "__all__"
