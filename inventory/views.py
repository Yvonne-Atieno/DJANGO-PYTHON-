
from django.shortcuts import render
from.forms import ProductUploadForm
# Create your views here.
def product_upload_view(request):
    form =ProductUploadForm()
    return render(request,"inventory/product_upload.html",{"form":form})