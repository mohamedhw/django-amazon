from datetime import datetime
from django.db import models
from django.contrib.auth.models import User







class Product(models.Model):
    name    = models.CharField(max_length=50)
    price   = models.IntegerField()
    image  = models.ImageField(upload_to='product_image', default='blaceholder.png')
    digital = models.BooleanField(default=False, blank=False, null=True)

    def __str__(self):
        return self.name 





class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    

    def __str__(self):
        return self.name 





class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(default=datetime.now)
    complete = models.BooleanField(default=False, blank=False)
    transactions_id = models.CharField(max_length=200, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


    def __str__(self):
        return str(self.id)



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(default=datetime.now)


    @property
    def get_total(self):
        total = self.product.price * self.quantity

        return total

    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.address
