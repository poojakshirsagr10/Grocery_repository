from django.urls import path
from .views import Add_product, GroceryList,GroceryUpdate,GroceryDeleteView

urlpatterns=[
    path("add/",Add_product.as_view()),
    path("list/",GroceryList.as_view()),
    path('update/<pk>/',GroceryUpdate.as_view()),
    path("delete/<pk>/",GroceryDeleteView.as_view())


]