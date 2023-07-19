from django.urls import path
from.views import product_upload_view
urlpatterns=[
    path("products/upload/",product_upload_view,name="product_uploadview"),
]