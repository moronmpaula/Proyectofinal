from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.Principal, name="Principal"),	
	path('Tienda/', views.Tienda, name="Tienda"),
	path('Carrito/', views.Carrito, name="Carrito"),
	path('Checkout/', views.Checkout, name="Checkout"),
	path('update_item/' , views.updateItem, name="update_item")

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)