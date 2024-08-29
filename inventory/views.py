from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from django.db.models import Sum

class PurchaseListView(LoginRequiredMixin, ListView):
  model = Purchase
  template_name = "inventory/index.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["revenue"] = Purchase.objects.aggregate(revenue=Sum("menu_item__price"))["revenue"]
    if context["revenue"] is None:
      context["revenue"] = 0
      context["cost"] = 0
      context["profit"] = 0
    else:
      cost = 0
      for purchase in Purchase.objects.all():
        menu_item_instance = purchase.menu_item
        recipe_requirements = RecipeRequirement.objects.filter(menu_item=menu_item_instance)
        for requirement in recipe_requirements:
          cost += requirement.ingredient.unit_price * requirement.quantity
      context["cost"] = cost
      context["profit"] = context["revenue"] - context["cost"]
    context['active_page'] = self.request.path
    return context

class PurchaseCreateView(LoginRequiredMixin, CreateView):
  model = Purchase
  template_name = "inventory/add-purchase.html"
  form_class = PurchaseForm
  success_url = "/"

  def form_valid(self, form):
    menu_item_instance = form.cleaned_data['menu_item']
    recipe_requirements = RecipeRequirement.objects.filter(menu_item=menu_item_instance)
    for requirement in recipe_requirements:
      if requirement.ingredient.quantity < requirement.quantity:
        messages.error(self.request, 'Not enough ingredients!')
        return self.render_to_response(self.get_context_data(form=form))
    for requirement in recipe_requirements:
      requirement.ingredient.quantity -= requirement.quantity
      requirement.ingredient.save()
    return super().form_valid(form)

class MenuItemListView(LoginRequiredMixin, ListView):
  model = MenuItem
  template_name = "inventory/menu-items.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['active_page'] = self.request.path
    return context

class MenuItemCreateView(LoginRequiredMixin, CreateView):
  model = MenuItem
  template_name = "inventory/add-menu-item.html"
  form_class = MenuItemForm
  success_url = "/menu-items"

class MenuItemUpdateView(LoginRequiredMixin, UpdateView):
  model = MenuItem
  template_name = "inventory/update-menu-item.html"
  form_class = MenuItemForm
  success_url = "/menu-items"

class MenuItemDeleteView(LoginRequiredMixin, DeleteView):
  model = MenuItem
  template_name = "inventory/delete-menu-item.html"
  success_url = "/menu-items"

class RecipeRequirementCreateView(LoginRequiredMixin, CreateView):
  model = RecipeRequirement
  template_name = "inventory/add-recipe-requirement.html"
  form_class = RecipeRequirementForm
  success_url = "/menu-items"

  def get_context_data(self):
    context = super().get_context_data()
    context["menu_item"] = self.kwargs["item_name"]
    return context

  def form_valid(self, form):
    menu_item_name = self.kwargs["item_name"]
    print(menu_item_name)
    menu_item = MenuItem.objects.get(name=menu_item_name)
    form.instance.menu_item = menu_item
    return super().form_valid(form)

class RecipeRequirementUpdateView(LoginRequiredMixin, UpdateView):
  model = RecipeRequirement
  template_name = "inventory/update-recipe-requirement.html"
  form_class = RecipeRequirementForm
  success_url = "/menu-items"

  def get_context_data(self):
    context = super().get_context_data()
    context["menu_item"] = self.kwargs["item_name"]
    return context

class RecipeRequirementDeleteView(LoginRequiredMixin, DeleteView):
  model = RecipeRequirement
  template_name = "inventory/delete-recipe-requirement.html"
  success_url = "/menu-items"

  def get_context_data(self, **kwargs):
    context = super().get_context_data()
    context["menu_item"] = self.kwargs["item_name"]
    print(context)
    return context

class IngredientListView(LoginRequiredMixin, ListView):
  model = Ingredient
  template_name = "inventory/ingredients.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['active_page'] = self.request.path
    return context

class IngredientCreateView(LoginRequiredMixin, CreateView):
  model = Ingredient
  template_name = "inventory/add-ingredient.html"
  form_class = IngredientForm
  success_url = "/ingredients"

class IngredientUpdateView(LoginRequiredMixin, UpdateView):
  model = Ingredient
  template_name = "inventory/update-ingredient.html"
  form_class = IngredientForm
  success_url = "/ingredients"

class IngredientDeleteView(LoginRequiredMixin, DeleteView):
  model = Ingredient
  template_name = "inventory/delete-ingredient.html"
  success_url = "/ingredients"

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

def logout_view(request):
  logout(request)
  return redirect("/")