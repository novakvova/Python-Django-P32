from django.shortcuts import render

from .forms import ProductForm

# Create your views here.
def app_product(request):
    form = ProductForm()
    return render(request, "add_product.html", {"form": form})