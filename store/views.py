from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import *
 
 
def Principal(request):
	context = {}
	return render(request, 'store/Principal.html', context)

def Tienda(request):

	if request.user.is_authenticated: 
		customer = request.user.customer
		order, created = Order.objects.get_or_create(custumer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0 }
		cartItems = order ['get_cart_items']
		
	products = Product.objects.all()
	context = {'products': products, 'cartItems' : cartItems}	
	return render(request, 'store/Tienda.html', context)

def Carrito(request):
	
	if request.user.is_authenticated: 
		customer = request.user.customer
		order, created = Order.objects.get_or_create(custumer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0  }
		cartItems = order ['get_cart_items']
		
	context = {'items':items, 'order':order, 'cartItems' : cartItems}
	return render(request, 'store/Carrito.html', context)

def Checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(custumer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items

	else:
		items = []
		order = {'get_cart_total': 0, 'get_cart_items': 0 }
		cartItems = order ['get_cart_items']


	context = {'items':items, 'order':order, 'cartItems' : cartItems}	
	return render(request, 'store/Checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(custumer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item fue agregado' , safe=False)
