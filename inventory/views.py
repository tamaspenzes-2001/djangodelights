from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
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
        cost += requirement.ingredient.price * requirement.quantity
    context["cost"] = cost
    context["profit"] = context["revenue"] - context["cost"]
    return context

class PurchaseCreateView(CreateView):
  model = Purchase
  template_name = "inventory/add_purchase.html"
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