from django.contrib import admin
from .models import Order
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("price","date_created","date_updated")
admin.site.register(Order,OrderAdmin)
