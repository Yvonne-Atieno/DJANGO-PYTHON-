from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from.forms import CartUploadForm
from .models import Cart

# Create your views here.
def cart_upload_view(request):
    if request.method == "POST":
        form =CartUploadForm()
        if form.is_valid():
            form.save()
    else:
        form = CartUploadForm()
    return render(request,"inventory/cart_upload.html",{"form":form})

def carts_list(request):
    carts = Cart.objects.all()
    return render(request,"inventory/carts_list.html",
    {"carts":carts})

def cart_detail_view(request,id):
    cart = Cart.objects.get(id=id)
    return render (request, "inventory/carts_details.html",
    {"cart":cart})