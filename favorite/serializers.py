from rest_framework import serializers

from favorite.models import FavoriteItems


class FavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItems
        fields = ['product', 'user', 'created_at']