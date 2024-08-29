from django import forms
from .models import *

class PurchaseForm(forms.ModelForm):
  class Meta:
    model = Purchase
    fields = "__all__"

class MenuItemForm(forms.ModelForm):
  class Meta:
    model = MenuItem
    fields = "__all__"

class RecipeRequirementForm(forms.ModelForm):
  class Meta:
    model = RecipeRequirement
    fields = ("ingredient", "quantity")

class IngredientForm(forms.ModelForm):
  class Meta:
    model = Ingredient
    fields = "__all__"
