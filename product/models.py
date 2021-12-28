from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    category = models.ForeignKey(Category,
                                 on_delete=models.RESTRICT,
                                 related_name='products')
    image = models.ImageField(upload_to='products',
                              null=True,
                              blank=True)
    view_count = models.IntegerField(default=1, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# Отзыв (Feedback)
class Comment(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField()

    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)



class Like(models.Model):
    user = models.ForeignKey(User,
                             related_name='likes',
                             on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like_count = models.PositiveIntegerField()

class LikeModel(models.Model):
    product = models.ForeignKey(Product, related_name="like_product", on_delete=models.CASCADE)
    like_status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name="user_like", on_delete=models.CASCADE)