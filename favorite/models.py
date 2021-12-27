from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product

User = get_user_model()


class FavoriteItems(models.Model):
    product = models.ForeignKey(Product, related_name="favorite_prod", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="favorite_user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
