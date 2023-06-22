from django.contrib import admin

# Register your models here.
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("payment","stock","price","date_created","date_updated","description")
admin.site.register(Payment,PaymentAdmin)
