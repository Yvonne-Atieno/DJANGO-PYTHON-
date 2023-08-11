from django.urls import path
from.views import product_upload, product_detail
from.views import products_list

urlpatterns=[
    path("products/upload/",product_upload,name="product_upload_view"),
    path("products/list/", products_list, name="products_list_view"),
    path("products/<int:id>/",product_detail, name="product_details_view"),
]
  
