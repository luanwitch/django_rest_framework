from rest_framework import serializers
from .models import Order, OrderItem, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price_at_purchase']
        read_only_fields = ['price_at_purchase']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=False)
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'user_name', 'order_date', 'status', 'total_amount', 'items']
        read_only_fields = ['total_amount']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        total_amount = 0
        for item_data in items_data:
            product = item_data.get('product')
            price = product.price # Agora o campo existe no modelo!
            
            OrderItem.objects.create(
                order=order, 
                price_at_purchase=price, 
                **item_data
            )
            total_amount += price * item_data.get('quantity')
            
        order.total_amount = total_amount
        order.save()
        return order