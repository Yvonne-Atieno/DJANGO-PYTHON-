

# Create your views here.
from django.shortcuts import render
from.forms import PaymentUploadForm
from inventory.models import Payment

# Create your views here.
def payment_upload_view(request):
    if request.method == "POST":
        form =PaymentUploadForm()
        if form.is_valid():
            form.save()
    else:
        form = PaymentUploadForm()
    return render(request,"inventory/payment_upload.html",{"form":form})

def payments_list(request):
    payments = Payment.objects.all()
    return render(request,"inventory/payments_list.html",
    {"payments":payments})

def payment_detail_view(request,id):
    payment = Payment.objects.get(id=id)
    return render (request, "inventory/payments_details.html",
    {"payment":payment})