from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/signup', SignUp.as_view(), name="signup"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('accounts/logout', logout_view, name="logout"),
    path('', PurchaseListView.as_view(), name="purchases"),
    path('add-purchase', PurchaseCreateView.as_view(), name="add_purchase"),
    path('menu-items', MenuItemListView.as_view(), name="menu_items"),
    path('menu-items/add', MenuItemCreateView.as_view(), name="add_menu_item"),
    path('menu-items/<pk>/update', MenuItemUpdateView.as_view(), name="update_menu_item"),
    path('menu-items/<pk>/delete', MenuItemDeleteView.as_view(), name="delete_menu_item"),
    path('menu-items/<item_name>/recipe-requirements/add', RecipeRequirementCreateView.as_view(), name="add_recipe_requirement"),
    path('menu-items/<item_name>/recipe-requirements/<pk>/update', RecipeRequirementUpdateView.as_view(), name="update_recipe_requirement"),
    path('menu-items/<item_name>/recipe-requirements/<pk>/delete', RecipeRequirementDeleteView.as_view(), name="delete_recipe_requirement"),
    path('ingredients', IngredientListView.as_view(), name="ingredients"),
    path('ingredients/add', IngredientCreateView.as_view(), name="add_ingredient"),
    path('ingredients/<pk>/update', IngredientUpdateView.as_view(), name="update_ingredient"),
    path('ingredients/<pk>/delete', IngredientDeleteView.as_view(), name="delete_ingredient"),
]