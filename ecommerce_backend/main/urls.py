from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("customer-address", views.CustomerAddressViewSet)
router.register("product-rating", views.ProductRatingViewSet)

urlpatterns = [
    path("vendors/", views.VendorList.as_view()),
    path("vendor/<int:pk>", views.VendorDetail.as_view()),
    path("vendor/register/", views.vendor_regsiter, name = "vendor_register"),
    path("vendor/login/", views.vendor_login, name = "vendor_login"),
    path("categories/", views.ProductCategoryList.as_view()),
    path("category/<int:pk>", views.ProductCategoryDetail.as_view()),
    path("products/", views.ProductList.as_view()),
    path("latest-products/", views.LatestProductList.as_view()),
    path("products/<str:tag>", views.TagProductList.as_view()),
    path("product/<int:pk>", views.ProductDetail.as_view()),
    path("product/add-img", views.AddProductImage),
    path("related-products/<int:pk>", views.RelatedProductList.as_view()),
    path("customers/", views.CustomerList.as_view()),
    path("customer/login/", views.customer_login, name = "customer_login"),
    path("customer/register/", views.customer_regsiter, name = "customer_register"),
    path("customer/<int:pk>", views.CustomerDetail.as_view()),
    path("user/<int:pk>", views.UserDetail.as_view()),
    path("orders/", views.OrderList.as_view()),
    path("order-items/", views.OrderItemList.as_view()),
    path("customer/<int:pk>/orders/", views.CustomerOrderItemList.as_view()),
    path("order/<int:pk>", views.OrderDetail.as_view()),
    path("product/<int:pk>/update-product-downloads/", views.updateProductDownload, name="update-product-downloads"),
    path("wishlist/", views.WishlistList.as_view()),
    path("customer/<int:pk>/wishlist/", views.CustomerWishlistList.as_view()),
    path("check-in-wishlist/", views.CheckProductInWishList, name = "check_product_in_wishList"),
    path("remove-wishlist/", views.RemoveWishListItem, name = "remove_item_fro_wishlist"),
    path("customer/<int:pk>/address/", views.CustomerAddressList.as_view()),
    path("customer/mark-default-address/<int:pk>", views.MarkDefaultAddress),
    path("customer/dashboard/<int:pk>", views.CustomerDashboard),
]

urlpatterns += router.urls
