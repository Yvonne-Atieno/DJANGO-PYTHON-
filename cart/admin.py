from django.contrib import admin
from .models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ("name","price","date_created","date_updated")
admin.site.register(Cart,CartAdmin)