from django.urls import path

from favorite.views import CreateFavoriteView, FavoriteItemsList

urlpatterns = [
    path('favorite/', CreateFavoriteView.as_view()),
    path('favorite/<int:pk>/', FavoriteItemsList.as_view()),
]