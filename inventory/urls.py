from django.urls import path
from .views import *

urlpatterns = [
    path('', PurchaseListView.as_view(), name="purchases"),
    path('/add_purchase', PurchaseCreateView.as_view(), name="add_purchase")
]