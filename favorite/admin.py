from django.contrib import admin

from favorite.models import FavoriteItems
from product.models import Category, Product

class Favoriteadmin(admin.ModelAdmin):
    list_display = ('product', "user", "created_at")

# Register your models here.
admin.site.register(FavoriteItems, Favoriteadmin)
