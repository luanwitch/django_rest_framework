from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price_at_purchase']
        read_only_fields = ['price_at_purchase'] # Preço deve ser definido na criação do item

class OrderSerializer(serializers.ModelSerializer):
    # Aninha os itens do pedido no serializer principal
    items = OrderItemSerializer(many=True, read_only=False)
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'user_name', 'order_date', 'status', 'total_amount', 'items']
        read_only_fields = ['total_amount']

    # Método para criar o Pedido e os Itens aninhados
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        total_amount = 0
        for item_data in items_data:
            product = item_data.get('product')
            # Busca o preço atual do produto para registrar no OrderItem
            price = product.price # Assumindo que seu modelo Product tem um campo 'price'
            
            OrderItem.objects.create(
                order=order, 
                price_at_purchase=price, 
                **item_data
            )
            total_amount += price * item_data.get('quantity')
            
        order.total_amount = total_amount
        order.save()
        return order