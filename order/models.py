from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product

User = get_user_model()


class OrderItem(models.Model):
    order = models.ForeignKey('Order',
                              on_delete=models.RESTRICT,
                              related_name='items')
    product = models.ForeignKey(Product,
                                on_delete=models.RESTRICT)
    quantity = models.SmallIntegerField(default=1)


STATUS_CHOICES = (
    ('open', 'Открыт'),
    ('in_process', 'В обработке'),
    ('closed', 'Закрыт')
)


class Order(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.RESTRICT,
                             related_name='orders')
    products = models.ManyToManyField(Product, through=OrderItem)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES)


