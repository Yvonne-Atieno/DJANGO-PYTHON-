from django.contrib import admin
from .models import Vendor
# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ("stock","price","date_created")
admin.site.register(Vendor,VendorAdmin)