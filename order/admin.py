from django.contrib import admin

from order.models import Order, OrderItem, CartItem

admin.site.register(Order)
admin.site.register(CartItem)
admin.site.register(OrderItem)
