from django import forms
from .models import *

class PurchaseForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(PurchaseForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-field'

  class Meta:
    model = Purchase
    fields = "__all__"

class MenuItemForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(MenuItemForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-field'

  class Meta:
    model = MenuItem
    fields = "__all__"

class RecipeRequirementForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(RecipeRequirementForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-field'

  class Meta:
    model = RecipeRequirement
    fields = ("ingredient", "quantity")

class IngredientForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(IngredientForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      visible.field.widget.attrs['class'] = 'form-field'

  class Meta:
    model = Ingredient
    fields = "__all__"
