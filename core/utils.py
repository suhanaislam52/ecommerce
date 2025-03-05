# your_app/utils.py

def calculate_total_price(cart_items, coupon_code):
    original_amount = sum(item.product.price * item.quantity for item in cart_items)
    
    discount = 0
    coupon_cost = 0

    if coupon_code == 'coupon1':
        discount = 0.10
        coupon_cost = 10
    elif coupon_code == 'coupon2':
        discount = 0.20
        coupon_cost = 15
    elif coupon_code == 'coupon3':
        discount = 0.15
        coupon_cost = 7

    return original_amount - (original_amount * discount) + coupon_cost
