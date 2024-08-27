from django.urls import path
from .views import *

urlpatterns = [
    path('', PurchaseListView.as_view(), name="purchases"),
    path('/add-purchase', PurchaseCreateView.as_view(), name="add_purchase"),
    path('/menu-items', MenuItemListView.as_view(), name="menu_items"),
    path('/menu-items/add', MenuItemCreateView.as_view(), name="add_menu_item"),
    path('/menu-items/<pk>/update', MenuItemUpdateView.as_view(), name="update_menu_item"),
    path('/menu-items/<pk>/delete', MenuItemDeleteView.as_view(), name="delete_menu_item")
]