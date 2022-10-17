from dataclasses import fields
from rest_framework import serializers
from .models import Category,Product,Cart
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('Username already exists')
        
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email already exists')

        return data

    def create(self,validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data

class LoginSerializer(serializers.Serializer):
    username =serializers.CharField()
    password=serializers.CharField()

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        # fields = (
        #     'id',
        #     'title'
        # )

        model = Category 
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    #createdby=serializers.ReadOnlyField(source='createdby.username',read_only=False)
    
    class Meta:
        model = Product
        fields = '__all__'
        
    
    def validate(self, data):
        specialcharacter="!@#$%^&*()_-=+<>?/~"
        if any(c in specialcharacter for c in data['name']):
            raise serializers.ValidationError('Name shouldnot contain any spl characters')

        return data



class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True,queryset=Product.objects.all())
    class Meta:
        model = User
        fields=('id','username','email','products')

class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','email')

class CartSerializer(serializers.ModelSerializer):
    cart_id = CartUserSerializer(read_only=True,many=True)
    products=ProductSerializer(read_only=True,many=True)
    class Meta:
        model = Cart
        fields=('cart_id','created','products')
