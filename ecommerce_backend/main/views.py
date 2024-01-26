from django.shortcuts import render
from rest_framework import generics, pagination, viewsets
from . import serializers
from . import models
from .custom_pagination import CustomPagination
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse 
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User  


# Vendor Views
class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer



@csrf_exempt
def vendor_regsiter(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    address = request.POST.get('address')
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        if user:
            try:
                # vendor_count = models.Vendor.objects.filter(address=address).count()
                # if vendor_count > 0:
                #     raise IntegrityError("Mobile number already exists")
                
                vendor = models.Vendor.objects.create(user = user, address = address)
                msg = {"auth": True, "msg": "succesful", "user":user.id, "vendor":vendor.id }
            except IntegrityError:
                msg = {"auth":False, "msg": "Mobile Already Used"}
        else:
            msg = {"auth":False, "msg": "Oops!! Something went wrong"}
    except IntegrityError:
        msg = {"auth":False, "msg": "Username Already Takken"}

    return JsonResponse(msg)


@csrf_exempt
def vendor_login(request):
    print("hhh")
    username = request.POST.get('username')
    password = request.POST.get('password')

    user= authenticate(request, username=username, password=password)
    print(user)
    if user:
        try:
            Vendor = models.Vendor.objects.get(user=user)
            msg = {
        "auth": True,
        "id":Vendor.id,
        }
        except:
            msg = {
        "auth": True,
        "id":user.id,
        "user_id":True
        }
        
    else:
        msg = {
        "auth": False,
        "msg":'invalid Password/Username',
        "id":None,
        }
    return JsonResponse(msg)


# Product Views
class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.GET.get('category')
        fetch_limit = self.request.GET.get('fetch_limit')

        if category:
            category_id = models.ProductCategory.objects.get(id=category)
            qs = qs.filter(ProductCategory=category_id)
        if fetch_limit:
            return qs[:int(fetch_limit)]
        

        return qs
# Latest Product Views
class LatestProductList(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = CustomPagination


    def get_queryset(self):
        qs = super().get_queryset()
        fetch_limit = self.request.GET.get('fetch_limit')
        if fetch_limit:
            # self.pagination_class = None
            return qs[:int(fetch_limit)]
        

class TagProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        tag = self.kwargs['tag']
        qs = qs.filter(tags__icontains=tag)
        return qs

class RelatedProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        qs = super().get_queryset()
        product_id = self.kwargs['pk']
        product = models.Product.objects.get(id=product_id)
        qs = qs.filter(ProductCategory=product.ProductCategory).exclude(id=product.id)
        return qs


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer


# Customer Views


class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

@csrf_exempt
def customer_login(request):
    print("hhh")
    username = request.POST.get('username')
    password = request.POST.get('password')

    user= authenticate(request, username=username, password=password)
    print(user)
    if user:
        try:
            customer = models.Customer.objects.get(user=user)
            msg = {
        "auth": True,
        "id":customer.id,
        }
        except:
            msg = {
        "auth": True,
        "id":user.id,
        "user_id":True
        }
        
    else:
        msg = {
        "auth": False,
        "msg":'invalid Password/Username',
        "id":None,
        }
    return JsonResponse(msg)

@csrf_exempt
def customer_regsiter(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    mobile = request.POST.get('mobile')
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        if user:
            try:
                customer_count = models.Customer.objects.filter(mobile=mobile).count()
                if customer_count > 0:
                    raise IntegrityError("Mobile number already exists")
                
                customer = models.Customer.objects.create(user = user, mobile = mobile)
                msg = {"auth": True, "msg": "succesful", "user":user.id, "customer":customer.id }
            except IntegrityError:
                msg = {"auth":False, "msg": "Mobile Already Used"}
        else:
            msg = {"auth":False, "msg": "Oops!! Something went wrong"}
    except IntegrityError:
        msg = {"auth":False, "msg": "Username Already Takken"}

    return JsonResponse(msg)




    
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerDetailSerializer

#user View
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = serializers.UserSerializer
# Order View


class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer




class OrderItemList(generics.ListCreateAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer




class CustomerOrderItemList(generics.ListAPIView):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        qs = super().get_queryset()
        user_id = self.kwargs['pk'] 
        qs = qs.filter(order__customer__id=user_id)
        return qs    
    

class OrderDetail(generics.ListAPIView):
    serializer_class = serializers.OrderDetailSerializer

    def get_queryset(self):
        order_id = self.kwargs["pk"]
        order = models.Order.objects.get(id=order_id)
        order_item = models.OrderItem.objects.filter(order=order.id)
        return order_item


# CustomerAddress
class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = models.CustomerAddress.objects.all()
    serializer_class = serializers.CustomerAddressSerializer


# ProductRating
class ProductRatingViewSet(viewsets.ModelViewSet):
    queryset = models.ProductRating.objects.all()
    serializer_class = serializers.ProductRatingSerializer


# ProductCategory Views
class ProductCategoryList(generics.ListCreateAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategorySerializer
    pagination_class = CustomPagination


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategoryDetailSerializer



@csrf_exempt
def updateProductDownload(request, pk):
    if request.method == 'POST':
        product_id = pk
        product = models.Product.objects.get(id=product_id)
        downloads = product.downloads
        downloads += 1
        models.Product.objects.filter(id=product_id).update(downloads=downloads)
        updated_product = models.Product.objects.get(id=product_id)
        total_downloads = updated_product.downloads
        return JsonResponse({"msg":True, "downloads":total_downloads})
    return JsonResponse( {"msg":False})



class WishlistList(generics.ListCreateAPIView):
    queryset = models.Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer
    pagination_class = CustomPagination


class CustomerWishlistList(generics.ListCreateAPIView):
    queryset = models.Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        customer_id = self.kwargs["pk"]
        qs = models.Wishlist.objects.filter(customer__id=customer_id)
        return qs 

#Customer Address 
class CustomerAddressList(generics.ListCreateAPIView):
    queryset = models.CustomerAddress.objects.all()
    serializer_class = serializers.CustomerAddressSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        customer_id = self.kwargs["pk"]
        qs = models.CustomerAddress.objects.filter(customer__id=customer_id)
        return qs 

@csrf_exempt
def CheckProductInWishList(request):
    customer_id = request.POST.get('customer')
    product_id = request.POST.get('product')

    check = models.Wishlist.objects.filter(product__id = product_id, customer__id = customer_id).count()
    msg = {
        "bool": False,
        }
    if check > 0:
        msg = {
        "bool": True,
        }
    return JsonResponse(msg)

@csrf_exempt
def RemoveWishListItem(request):
    customer_id = request.POST.get('customer')
    product_id = request.POST.get('product')

    check = models.Wishlist.objects.filter(product__id = product_id, customer__id = customer_id).delete()
    msg = {
        "bool": False,
        }
    if check:
        msg = {
        "bool": True,
        }
    return JsonResponse(msg)


@csrf_exempt
def AddProductImage(request):
    product_id = request.POST.get('pk')
    product_image = request.FILES.get('image')

    product = models.Product.objects.get(pk = product_id)
    productImage = models.ProductImage.objects.create(product = product, image = product_image)
    msg = {
        "id": product_id,
        }
    if productImage:
        msg["img"] = productImage.image.url
    return JsonResponse(msg)

@csrf_exempt
def MarkDefaultAddress(request,pk):
    models.CustomerAddress.objects.all().update(default_address=False)
    check = models.CustomerAddress.objects.filter(id=pk).update(default_address=True)
    msg = {
        "bool": False,
        }
    if check:
        msg = {
        "bool": True,
        }
    return JsonResponse(msg)


@csrf_exempt
def CustomerDashboard(request,pk):

    totalAddresses = models.CustomerAddress.objects.filter(customer__id = pk).count()
    totalWishlist = models.Wishlist.objects.filter(customer__id = pk).count()
    totalOrders = models.Order.objects.filter(customer__id = pk).count()
    msg = {
        "totalAddresses": totalAddresses,
        "totalWishlist": totalWishlist,
        "totalOrders": totalOrders,
        }

    return JsonResponse(msg)