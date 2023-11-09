from django.contrib.auth.models import User, Group 
from restaurant.models import *
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'groups']

    # this line is added to ensure that the password is encrypted when the data is written to the database
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) 
        return user   

class GroupSetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    
    class Meta: 
        model = User
        fields = ['id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class MenuSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200, required=True)
    price = serializers.IntegerField(required=True)
    category = CategorySerializer(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
        
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'category', 'category_name']
        
class CartSerializer(serializers.ModelSerializer):
    itemName = serializers.CharField(source='itemId.name', read_only=True)    
    userName = serializers.CharField(source='userId.username', read_only=True)
    class Meta:
        model = Cart
        fields = ['userId', 'userName', 'itemId', 'itemName', 'quantity', 'unitPrice', 'price']
   
class CartItemsSerializer(serializers.ModelSerializer):
    itemId = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True)
    
    class Meta:
        model = Menu
        fields = ['itemId', 'quantity']
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'orderDate', 'totalPrice', 'status', 'deliveryId']
        
class OrderItemSerializer(serializers.ModelSerializer):
    itemName = serializers.CharField(source='itemId.name', read_only=True)        
    class Meta:
        model = OrderItem
        fields = ['orderId', 'itemId', 'itemName', 'quantity', 'unitPrice', 'price']
