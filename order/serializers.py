from rest_framework import serializers

from order.models import OrderItem, Order, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'owner']


class OrderItemSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, instance):
        return instance.order.user.pk

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'user']


class OrderSerializer(serializers.ModelSerializer):
    positions = OrderItemSerializer(write_only=True, many=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'positions', 'status']

    def create(self, validated_data):
        products = validated_data.pop('positions')
        user = self.context.get('request').user
        order = Order.objects.create(user=user, status='open')
        for prod in products:
            product = prod['product']
            quantity = prod['quantity']
            OrderItem.objects.create(order=order,
                                     product=product,
                                     quantity=quantity)
        return order

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['positions'] = OrderItemSerializer(instance.items.all(), many=True).data
        return representation
