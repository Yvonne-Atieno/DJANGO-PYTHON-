

# Create your views here.


# Create your views here.
from django.shortcuts import render
from.forms import orderUploadForm
from inventory.models import order

# Create your views here.
def order_upload(request):
    if request.method == "POST":
        form =orderUploadForm()
        if form.is_valid():
            form.save()
    else:
        form = orderUploadForm()
    return render(request,"inventory/order_upload.html",{"form":form})

def order_list(request):
    order = order.objects.all()
    return render(request,"inventory/order_list.html",
    {"orders":orders})

def order_detail(request,id):
    order = order.objects.get(id=id)
    return render (request, "inventory/order_details.html",
    {"order":order})