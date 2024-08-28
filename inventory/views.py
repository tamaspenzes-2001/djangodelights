from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.db.models import Sum

# Create your views here.
class PurchaseListView(ListView):
  model = Purchase
  template_name = "inventory/index.html"

  def get_context_data(self):
    context = super().get_context_data()
    context["revenue"] = Purchase.objects.aggregate(revenue=Sum("menu_item__price"))["revenue"]
    cost = 0
    for purchase in Purchase.objects.all():
      menu_item_instance = purchase.menu_item
      recipe_requirements = RecipeRequirement.objects.filter(menu_item=menu_item_instance)
      for requirement in recipe_requirements:
        cost += requirement.ingredient.unit_price * requirement.quantity
    context["cost"] = cost
    context["profit"] = context["revenue"] - context["cost"]
    return context

class PurchaseCreateView(CreateView):
  model = Purchase
  template_name = "inventory/add-purchase.html"
  form_class = PurchaseForm
  success_url = "/"

  def form_valid(self, form):
    menu_item_instance = form.cleaned_data['menu_item']
    recipe_requirements = RecipeRequirement.objects.filter(menu_item=menu_item_instance)
    for requirement in recipe_requirements:
      if requirement.ingredient.quantity < requirement.quantity:
        return HttpResponse("Not enough ingredients!")
    for requirement in recipe_requirements:
      requirement.ingredient.quantity -= requirement.quantity
    return super().form_valid(form)

class MenuItemListView(ListView):
  model = MenuItem
  template_name = "inventory/menu-items.html"

class MenuItemCreateView(CreateView):
  model = MenuItem
  template_name = "inventory/add-menu-item.html"
  form_class = MenuItemForm
  success_url = "/menu-items"

class MenuItemUpdateView(UpdateView):
  model = MenuItem
  template_name = "inventory/update-menu-item.html"
  form_class = MenuItemForm
  success_url = "/menu-items"

class MenuItemDeleteView(DeleteView):
  model = MenuItem
  template_name = "inventory/delete-menu-item.html"
  success_url = "/menu-items"

class RecipeRequirementCreateView(CreateView):
  model = RecipeRequirement
  template_name = "inventory/add-recipe-requirement.html"
  form_class = RecipeRequirementForm
  success_url = "/menu-items"

  def form_valid(self, form):
    menu_item_name = self.request.GET.get('menu_item_name')
    menu_item = MenuItem.objects.get(title=menu_item_name)
    form.instance.menu_item = menu_item
    return super().form_valid(form)

class RecipeRequirementUpdateView(UpdateView):
  model = RecipeRequirement
  template_name = "inventory/update-recipe-requirement.html"
  form_class = RecipeRequirementForm
  success_url = "/menu-items"

class RecipeRequirementDeleteView(DeleteView):
  model = RecipeRequirement
  template_name = "inventory/delete-recipe-requirement.html"
  success_url = "/menu-items"

class IngredientListView(ListView):
  model = Ingredient
  template_name = "inventory/ingredients.html"

class IngredientCreateView(CreateView):
  model = Ingredient
  template_name = "inventory/add-ingredient.html"
  form_class = IngredientForm
  success_url = "/ingredients"

class IngredientUpdateView(UpdateView):
  model = Ingredient
  template_name = "inventory/update-ingredient.html"
  form_class = IngredientForm
  success_url = "/ingredients"

class IngredientDeleteView(DeleteView):
  model = Ingredient
  template_name = "inventory/delete-ingredient.html"