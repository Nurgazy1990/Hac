from django.contrib import admin
from product.models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', "description", "price", "view_count")

# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
