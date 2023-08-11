from django.db import models
from customer.models import Customer
from cart.models import Cart
# from Delivery.models import Delivery

# Create your models here.
class Order(models.Model):
    name= models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    customer = models.ForeignKey(Customer, null= True, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, null= True, on_delete = models.CASCADE) 
       
def _str_(self):
        return self.name 
       
    