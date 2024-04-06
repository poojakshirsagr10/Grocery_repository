from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Grocery

class Add_product(CreateView):
    model = Grocery
    fields = "__all__"

class GroceryList(ListView):
    model = Grocery


class GroceryUpdate(UpdateView):
    model= Grocery
    fields=("__all__")

    success_url="/"

class GroceryDeleteView(DeleteView):
    model = Grocery
    success_url = "/"


