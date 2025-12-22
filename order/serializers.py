from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'product_name', 'quantity', 'price_at_purchase']
        read_only_fields = ['price_at_purchase']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'user_name', 'order_date', 'status', 'total_amount', 'items']
        read_only_fields = ['total_amount']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        total = 0
        for item in items_data:
            product = item['product']
            price = product.price

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
                price_at_purchase=price
            )
            total += price * item['quantity']

        order.total_amount = total
        order.save()
        return order
