from rest_framework import serializers
from .models import User,Item,Order,OrderItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class ProductUpdateSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=False)
    photo = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.CharField(required=False)
    category_name = serializers.CharField(required=False)
    category_code = serializers.CharField(required=False)
    subcategory_code = serializers.CharField(required=False)
    subcategory_name = serializers.CharField(required=False)

    class Meta:
        model = Item
        fields = (
            "name",
            "photo",
            "description",
            "price",
            "category_name",
            "category_code",
            "subcategory_code",
            "subcategory_name",
        )

