from django.db import models
from django.contrib.auth.models import User
from djstripe.models import PaymentIntent
from django.conf import settings
from django.urls import reverse
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/',blank=True, null=True)
    stock = models.IntegerField(default=0)  # Add this line

    def __str__(self):
        return self.name
    def is_in_stock(self):
        return self.stock > 0  # Add this method
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart of {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} in {self.cart.user.username}\'s cart'
    

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product', through='WishlistItem')

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    shipping_address = models.CharField(max_length=255, default='Not Provided')
    phone_number = models.CharField(max_length=20, default='Not Provided')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_status = models.CharField(
        max_length=20,
        choices=[('To be Delivered', 'To be Delivered'), ('Delivered', 'Delivered')],
        default='To be Delivered'
    )

    def __str__(self):
        return f"Order {self.id} - ${self.total_price}"
    
class OrderDetail(models.Model):
    ORDER_STATUS_CHOICES = [
        ('to_be_delivered', 'To Be Delivered'),
        ('delivered', 'Delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50, default='pending')
    delivery_status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default='to_be_delivered'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.username} - ${self.total_price}"
    

class Coupon(models.Model):
    code = models.CharField(max_length=20)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    terms = models.TextField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.code
    
class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.address

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint by {self.name} on {self.created_at}"