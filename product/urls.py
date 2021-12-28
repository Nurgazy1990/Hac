from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (ProductViewSet, CategoryViewSet,
                    CommentViewSet, LikeView, LikeItemView)


router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('like/', LikeItemView.as_view())
]
