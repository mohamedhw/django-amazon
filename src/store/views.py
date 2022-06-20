from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import *





def store(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, "store/store.html", context)



def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items,
        'order': order,
    }

    return render(request, "store/cart.html", context)



def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {
        'items': items,
        'order': order,
    }

    return render(request, "store/checkout.html", context)



def updateitem(request):
    return JsonResponse('Item was added', safe=False)




# function to add product to the cart

def add_to_cart(request, pk):

    product = get_object_or_404(Product, pk=pk) # get the product and add it to var

    order_item = OrderItem.objects.create(product=product) # create order iteams model for the user 

    order_qs = Order.objects.filter(customer=request.user, ordered=False) # asine the order to the user 

    if order_qs.exists():
        order = order_qs[0]
        if order_item in order:
            order_item.quantity += 1
            order_item.save()
    else:
        order = Order.objects.create(customer=request.user)
        order.product.add(order_item)

    return redirect("cart", kwargs={'pk':pk}) 
    

