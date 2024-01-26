from rest_framework import serializers
from . import models
from django.contrib.auth.models import User




#Vendor
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = "__all__"
#User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    


class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


#ProductImage
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = "__all__"


#Product
class ProductSerializer(serializers.ModelSerializer):
    product_imgs = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = models.Product
        fields = ["id","ProductCategory","Vendor","title","description","price","product_imgs","file","downloads","tags","tag_list","demo_url"]


class ProductDetailSerializer(serializers.ModelSerializer):
    product_imgs = ProductImageSerializer(many=True, read_only=True)
    product_rating = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = ["id","ProductCategory","Vendor","title","description","price","tag_list","demo_url","product_rating","product_imgs","file","downloads"]
    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


# Customer Serializer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = "__all__"


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response

    # def __init__(self, *args, **kwargs):
    #     super(CustomerDetailSerializer, self).__init__(*args, **kwargs)
    #     self.Meta.depth = 1


# Order & OrderItem
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()
    order = OrderSerializer()

    class Meta:
        model = models.OrderItem
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(OrderItemSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1    


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


# CustomerAddressSerializer
class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddress
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(CustomerAddressSerializer, self).__init__(*args, **kwargs)
    #     self.Meta.depth = 1


# ProductRatingSerializer
class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

#ProductCategory 
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = "__all__"


class ProductCategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductCategoryDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1




class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wishlist
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializer(instance.customer).data
        response['product'] = ProductSerializer(instance.product).data
        return response
