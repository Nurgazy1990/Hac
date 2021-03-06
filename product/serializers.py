from rest_framework import serializers

from product.models import Product, Category, Comment, Like, LikeModel


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['product', 'text', 'rating']

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError('Рейтинг должен быть от 1 до 5')
        return rating

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['author'] = user
        return super().create(validated_data)



class LikeSerializer(serializers.Serializer):

    def validate_product_id(self, product_id):
        if Like.objects.filter(pk=product_id).exists():
            Like.like_count += 1
            Like.save()
        return Like.like_count

class LikeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = ['product', 'like_status']