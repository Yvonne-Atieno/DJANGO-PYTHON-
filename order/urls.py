from django.urls import path
from.views import order_upload_view, order_detail_view
from.views import order_list

urlpatterns=[
    path("orders/upload/",order_upload_view,name="order_uploadview"),
    path("orders/list/", order_list, name="order_list"),
    path("orders/<int:id>/",order_detail_view, name="order_details"),
]