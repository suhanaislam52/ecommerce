from django.shortcuts import get_object_or_404
from .models import Product  # Import your product model

def add_to_cart(cart, product_id, quantity):
    """Add a product to the cart."""
    product = get_object_or_404(Product, id=product_id)
    if product_id in cart:
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id] = {'quantity': quantity, 'price': str(product.price)}

def remove_from_cart(cart, product_id):
    """Remove a product from the cart."""
    if product_id in cart:
        del cart[product_id]

def get_cart_total(cart):
    """Calculate the total price of the cart."""
    total = sum(float(item['price']) * item['quantity'] for item in cart.values())
    return total
