from django.contrib import admin
from .models import Product, Cart, CartItem, Wishlist, WishlistItem
from .models import OrderDetail
from .models import Coupon
from .models import ContactInfo, Complaint

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')  # Customize as needed
    fields = ('name', 'description', 'price', 'stock')  # Include the fields to be edited
    readonly_fields = ('is_in_stock',)  # Optional: make `is_in_stock` read-only if you prefer

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')  # Customize as needed

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')  # Customize as needed

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Customize as needed

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('wishlist', 'product', 'added_at')  # Customize as needed

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'shipping_address', 'phone_number', 'total_price', 'payment_status', 'delivery_status', 'created_at')
    list_filter = ('delivery_status', 'payment_status')
    search_fields = ('user__username', 'shipping_address', 'phone_number')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('user', 'shipping_address', 'phone_number', 'total_price', 'payment_status', 'delivery_status')
        }),
        ('Date Information', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'terms', 'purchase_price')
    fields = ('code', 'discount', 'terms', 'purchase_price')
    readonly_fields = ()  # You can add fields to be readonly if needed

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')
    fields = ('address', 'phone', 'email')

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
