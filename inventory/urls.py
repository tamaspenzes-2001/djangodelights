from django.urls import path
from .views import *

urlpatterns = [
    path('', PurchaseListView.as_view()),
]