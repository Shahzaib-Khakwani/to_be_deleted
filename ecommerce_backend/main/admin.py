from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Vendor)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductImage)

class ProductImageInline(admin.StackedInline):
    model = models.ProductImage

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"title": ["title"]}
    inlines = [ProductImageInline]

admin.site.register(models.Product, ProductAdmin)


admin.site.register(models.Order)
admin.site.register(models.OrderItem)

admin.site.register(models.Customer)
admin.site.register(models.CustomerAddress)

admin.site.register(models.ProductRating)

class Wishlist(admin.ModelAdmin):
    list_display = ["id","customer", "product"]
admin.site.register(models.Wishlist, Wishlist)