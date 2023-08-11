from django.urls import path
from.views import cart_upload_view, cart_detail_view
from.views import carts_list

urlpatterns=[
    path("carts/upload/",cart_upload_view,name="cart_uploadview"),
    path("carts/list/", carts_list, name="carts_list"),
    path("carts/<int:id>/",cart_detail_view, name="cart_details"),
]
  