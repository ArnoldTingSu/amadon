from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    return redirect('/store')

def store(request):
    context = {
        "products": Product.objects.all(),
        "quantity": [1,2,3,4,5,6,7,8,9]
    }
    return render(request, 'index.html', context)

def process(request, id):
    if request.method =='POST':
        purchase_item = Product.objects.get(id=id)
        new_order = Order.objects.create(
            quantity=request.POST['quantity'],
            total_charge=int(request.POST['quantity'])*purchase_item.price)
        new_order.items_ordered.add(purchase_item)
        print(request.POST)
        return redirect('/store/checkout')
    else:
        return redirect('/store')

def success(request):
    all_orders= Order.objects.all()
    total_spent=0
    for order in all_orders:
        total_spent += order.total_charge
    context = {
        'last_order': Order.objects.last(),
        'all_orders': all_orders,
        'grand_total': total_spent
    }
    return render(request, "success.html", context)