from django.urls import path
from.views import payment_upload_view, payment_detail_view
from.views import payments_list

urlpatterns=[
    path("payments/upload/",payment_upload_view,name="payment_uploadview"),
    path("payments/list/", payments_list, name="payments_list"),
    path("payments/<int:id>/",payment_detail_view, name="payment_details"),
]
  