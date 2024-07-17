from django.contrib import admin
from .models import Vendor, ProductImages, Producto_Core, ProductReview, CartOrder, CartOrderItems, Category, whishlist, Address


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title','product_image' ,'price', 'status', 'products_status', 'featured','caterory']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','category_image','featured']
    
class VendorAdmin(admin.ModelAdmin):
    list_display = ['title','vendor_image']
    
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user','price', 'products_status']
    
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','invoice_no', 'item', 'image', 'qty', 'price', 'total']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'review', 'rating']

class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'date']

class AdderssAdmin(admin.ModelAdmin):
    list_display = ['user','address', 'status']
    

admin.site.register(Producto_Core, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(whishlist, wishlistAdmin)
admin.site.register(Address, AdderssAdmin)

    
    

