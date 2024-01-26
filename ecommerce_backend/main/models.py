from django.db import models
from django.contrib.auth.models import User


# Vendor
class Vendor(models.Model):
    """
    Vendor Model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
        return self.user.username


# ProductCategory
class ProductCategory(models.Model):
    """
    ProductCategory Model
    """

    title = models.CharField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title


# Product
class Product(models.Model):
    """
    Product Model
    """

    ProductCategory = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True, related_name="order_item"
    )
    Vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    tags = models.TextField()
    price = models.FloatField()
    demo_url = models.URLField(null=True, blank=True)
    file = models.FileField(upload_to="product_files/", null=True)
    image = models.ImageField(upload_to="product_imgs/" , null=True)
    downloads = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def tag_list(self):
        tagList = self.tags.split(',')
        return tagList

# customer


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.PositiveBigIntegerField()
    profile_img = models.ImageField(upload_to="customer_imgs/", null=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    order_status = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_item"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.product.title


# CustmerAddress


class CustomerAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer_address"
    )
    address = models.TextField()
    default_address = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.user.username


# ProductRating
class ProductRating(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="rating_customers"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_rating"
    )
    rating = models.PositiveIntegerField()
    review = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.review

# ProductImages
class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_imgs"
    )
    image = models.ImageField(upload_to="product_imgs/" , null=True)

    def __str__(self):
        return self.image.url


#Wishlist
class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "WishList"

    def __str__(self):
        return f"{self.customer.user.username} --- {self.product.title}"