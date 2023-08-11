

# Create your views here.
from django.shortcuts import render
from.forms import CustomerUploadForm
from inventory.models import Customer

# Create your views here.
def customer_upload_view(request):
    if request.method == "POST":
        form =CustomerUploadForm()
        if form.is_valid():
            form.save()
    else:
        form = CustomerUploadForm()
    return render(request,"inventory/product_upload.html",{"form":form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request,"inventory/customer_list.html",
    {"customer":customers})

def customer_detail_view(request,id):
    customer = Customer.objects.get(id=id)
    return render (request, "inventory/customer_details.html",
    {"customer":customer})