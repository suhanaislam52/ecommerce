from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem, Wishlist, WishlistItem
import stripe
from django.conf import settings
from django.http import JsonResponse
from .models import Order
from django.views.decorators.csrf import csrf_exempt
from .utils import calculate_total_price
from .forms import CheckoutForm
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from .models import OrderDetail
from .models import Coupon
from django.contrib import messages
from .models import ContactInfo, Complaint
from .forms import ComplaintForm





def index(request):
    return render(request, 'core/HomePage.html')

def category_view(request):
    return render(request, 'core/Category.html')

def header_view(request):
    return render(request, 'core/header.html')

def footer(request):
    return render(request, 'core/footer.html')

def food_view(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'core/food.html', {'products': products})

def makeup_page(request):
    return render(request, 'core/makeup.html')

def perfumes(request):
    return render(request, 'core/Perfumes.html')

def shoes(request):
    return render(request,'core/Shoes.html')

def cleaning(request):
    return render(request,'core/Cleaning.html')

def clothing(request):
    return render(request,'core/Clothing.html')

def games(request):
    return render(request,'core/Games.html')

def furnitures(request):
    return render(request,'core/Furnitures.html')

def Beverage(request):
    return render(request,'core/BeverageContainers.html')

def seafood_platter_view(request):
    product = get_object_or_404(Product, name="Seafood Platter")
    return render(request, 'core/SeaFoodPlatter.html', {'product': product})

def Salmon(request):
    # Fetch the product by name
    product = get_object_or_404(Product, name="Salmon with Shrimp")
    return render(request, 'core/Salmon.html', {'product': product})


def Chicken(request):
    product = get_object_or_404(Product, name="Smoked Grilled Chicken")
    return render(request,'core/Chicken.html',{'product': product})

def Sushi(request):
    product = get_object_or_404(Product, name="Salmon Sushi Roll")
    return render(request,'core/Sushi.html',{'product': product})

def Steak(request):
    product = get_object_or_404(Product, name="Beef Steak with Mashed Potato")
    return render(request,'core/BeefSteak.html',{'product': product})

def Shawarma(request):
    product = get_object_or_404(Product, name="Shawarma Roll")
    return render(request,'core/Shawarma.html',{'product': product})

def Sandwich(request):
    product = get_object_or_404(Product, name="Sub Sandwich")
    return render(request,'core/Sandwich.html',{'product': product})

def Burger(request):
    product = get_object_or_404(Product, name="Double Chicken Patty Burger")
    return render(request,'core/Burger.html',{'product': product})

def Croissant(request):
    product = get_object_or_404(Product, name="Croissant")
    return render(request,'core/Croissant.html',{'product': product})

def JarCake(request):
    product = get_object_or_404(Product, name="Rainbow Jar Cake")
    return render(request,'core/JarCake.html',{'product': product})

def christmascake(request):
    product = get_object_or_404(Product, name="Christmas Cake")
    return render(request,'core/christmascake.html',{'product': product})

def matt(request):
    product = get_object_or_404(Product, name="Red Matte Lipstick")
    return render(request, 'core/matt.html', {'product': product})

def peptide(request):
    product = get_object_or_404(Product, name="Peptide Lip Treatments")
    return render(request, 'core/peptide.html', {'product': product})
def concealer(request):
    product = get_object_or_404(Product, name="Perfect Blend Concealer")
    return render(request, 'core/concealer.html', {'product': product})
def highlighter(request):
    product = get_object_or_404(Product, name="Glistening Glow Highlighter")
    return render(request, 'core/highlighter.html', {'product': product})
def shadow(request):
    product = get_object_or_404(Product, name="Essential Eye Shadow Palette")
    return render(request, 'core/shadow.html', {'product': product})
def mascara(request):
    product = get_object_or_404(Product, name="Lash Sensational Waterproof Mascara")
    return render(request, 'core/mascara.html', {'product': product})
def cleanser(request):
    product = get_object_or_404(Product, name="Hydrating Cleanser")
    return render(request, 'core/cleanser.html', {'product': product})
def lotion(request):
    product = get_object_or_404(Product, name="Daily Moisturizing Body Lotion")
    return render(request, 'core/lotion.html', {'product': product})
def serum(request):
    product = get_object_or_404(Product, name="Shine Anti-Frizz Hair Serum")
    return render(request, 'core/serum.html', {'product': product})
def Beauty(request):
    product = get_object_or_404(Product, name="Beauty Body Collection")
    return render(request, 'core/Beauty.html', {'product': product})
def Lipshade(request):
    product = get_object_or_404(Product, name="Liquid Lip Color")
    return render(request, 'core/Lipshade.html', {'product': product})
def remover(request):
    product = get_object_or_404(Product, name="Micellar Makeup Remover")
    return render(request, 'core/remover.html', {'product': product})
def moonlight(request):
    product = get_object_or_404(Product, name="Moonlight Perfume")
    return render(request, 'core/moonlight.html', {'product': product})
def carolina(request):
    product = get_object_or_404(Product, name="Carolina Herrera Good Girl perfume")
    return render(request, 'core/carolina.html', {'product': product})
def chanel(request):
    product = get_object_or_404(Product, name="Chance Chanel")
    return render(request, 'core/chanel.html', {'product': product})
def wildflower(request):
    product = get_object_or_404(Product, name="Secret Wildflower")
    return render(request, 'core/wildflower.html', {'product': product})
def bleu(request):
    product = get_object_or_404(Product, name="Bleu de Chanel for Men")
    return render(request, 'core/bleu.html', {'product': product})
def gucci(request):
    product = get_object_or_404(Product, name="Gucci Guilty Intense")
    return render(request, 'core/gucci.html', {'product': product})
def vanilla(request):
    product = get_object_or_404(Product, name="Dirty Vanilla Roll-On")
    return render(request, 'core/vanilla.html', {'product': product})
def Perfumecollection(request):
    product = get_object_or_404(Product, name="Perfume Collection")
    return render(request, 'core/Perfumecollection.html', {'product': product})
def lux(request):
    product = get_object_or_404(Product, name="Lux Perfume Hamper")
    return render(request, 'core/lux.html', {'product': product})
def blackheels(request):
    product = get_object_or_404(Product, name="Classic Black Heels")
    return render(request, 'core/blackheels.html', {'product': product})
def whiteheels(request):
    product = get_object_or_404(Product, name="Chic White Heels")
    return render(request, 'core/whiteheels.html', {'product': product})
def elegantflats(request):
    product = get_object_or_404(Product, name="Elegant Black Flats")
    return render(request, 'core/elegantflats.html', {'product': product})
def ribbon(request):
    product = get_object_or_404(Product, name="Chic Ribbon Shoes")
    return render(request, 'core/ribbon.html', {'product': product})
def officeheels(request):
    product = get_object_or_404(Product, name="Office Heels")
    return render(request, 'core/officeheels.html', {'product': product})
def sneakers(request):
    product = get_object_or_404(Product, name="Urban Comfort Sneakers")
    return render(request, 'core/sneakers.html', {'product': product})
def lowheels(request):
    product = get_object_or_404(Product, name="Comfortable Low Heels")
    return render(request, 'core/lowheels.html', {'product': product})
def phillips(request):
    product = get_object_or_404(Product, name="Philips PowerGo Vacuum Cleaner")
    return render(request, 'core/phillips.html', {'product': product})
def brooms(request):
    product = get_object_or_404(Product, name="Cleaning Brooms")
    return render(request, 'core/brooms.html', {'product': product})
def glasscleaner(request):
    product = get_object_or_404(Product, name="Glass Cleaner")
    return render(request, 'core/glasscleaner.html', {'product': product})
def glasswiper(request):
    product = get_object_or_404(Product, name="Glass Wiper")
    return render(request, 'core/glasswiper.html', {'product': product})
def gloves(request):
    product = get_object_or_404(Product, name="Cleaning Gloves")
    return render(request, 'core/gloves.html', {'product': product})
def dishsoap(request):
    product = get_object_or_404(Product, name="DishSoap")
    return render(request, 'core/dishsoap.html', {'product': product})
def summer(request):
    product = get_object_or_404(Product, name="Yellow Summer Dress")
    return render(request, 'core/summer.html', {'product': product})
def gown(request):
    product = get_object_or_404(Product, name="Blue Gown")
    return render(request, 'core/gown.html', {'product': product})
def denims(request):
    product = get_object_or_404(Product, name="Blue Denims")
    return render(request, 'core/denims.html', {'product': product})
def officeattire(request):
    product = get_object_or_404(Product, name="Formal Attire for Women")
    return render(request, 'core/officeattire.html', {'product': product})
def jeans(request):
    product = get_object_or_404(Product, name="Black Jeans")
    return render(request, 'core/jeans.html', {'product': product})
def formalattire(request):
    product = get_object_or_404(Product, name="Formal Attire")
    return render(request, 'core/formalattire.html', {'product': product})
def PS5(request):
    product = get_object_or_404(Product, name="PS 5")
    return render(request, 'core/PS 5.html', {'product': product})
def chair(request):
    product = get_object_or_404(Product, name="Gaming Chair")
    return render(request, 'core/chair.html', {'product': product})
def headset(request):
    product = get_object_or_404(Product, name="Headset")
    return render(request, 'core/headset.html', {'product': product})
def keyboard(request):
    product = get_object_or_404(Product, name="Keyboard")
    return render(request, 'core/keyboard.html', {'product': product})
def controller(request):
    product = get_object_or_404(Product, name="Controller")
    return render(request, 'core/controller.html', {'product': product})
def gamingpackage(request):
    product = get_object_or_404(Product, name="Package")
    return render(request, 'core/gamingpackage.html', {'product': product})
def pc(request):
    product = get_object_or_404(Product, name="Gaming PC")
    return render(request, 'core/pc.html', {'product': product})
def singlesofa(request):
    product = get_object_or_404(Product, name="White Single Sofa")
    return render(request, 'core/singlesofa.html', {'product': product})
def bingbang(request):
    product = get_object_or_404(Product, name="Bing Bang Chair")
    return render(request, 'core/bingbang.html', {'product': product})
def coffeetable(request):
    product = get_object_or_404(Product, name="White Square Coffeetable")
    return render(request, 'core/coffeetable.html', {'product': product})
def desk(request):
    product = get_object_or_404(Product, name="Study Desk")
    return render(request, 'core/desk.html', {'product': product})
def livingsofa(request):
    product = get_object_or_404(Product, name="Living Room Sofa Set")
    return render(request, 'core/livingsofa.html', {'product': product})
def whitebed(request):
    product = get_object_or_404(Product, name="Bed With White Sheets")
    return render(request, 'core/whitebed.html', {'product': product})
def netany(request):
    product = get_object_or_404(Product, name="Netany Drinking Glass Set with Glass Straw (4 Pieces)")
    return render(request, 'core/netany.html', {'product': product})
def bamboo(request):
    product = get_object_or_404(Product, name="6-Piece Glass Set with Bamboo Lids")
    return render(request, 'core/bamboo.html', {'product': product})
def decemera(request):
    product = get_object_or_404(Product, name="Decemera Glass with Bamboo Lids")
    return render(request, 'core/decemera.html', {'product': product})
def luxu(request):
    product = get_object_or_404(Product, name="Luxu Drinking Glasses Set (13 Pieces)")
    return render(request, 'core/luxu.html', {'product': product})
def bottles(request):
    product = get_object_or_404(Product, name="Enhance Glass Water Bottles")
    return render(request, 'core/bottles.html', {'product': product})
def minibottles(request):
    product = get_object_or_404(Product, name="8 oz Juice Mini Bootles")
    return render(request, 'core/minibottles.html', {'product': product})
def glaver(request):
    product = get_object_or_404(Product, name="Glaver Moon’s Drinking Jars")
    return render(request, 'core/glaver.html', {'product': product})


from django.views.decorators.http import require_GET
@require_GET
def product_search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query)
    results = []
    
    for product in products:
        results.append({
            'name': product.name,
            'url': product.get_absolute_url()  # Ensure you have this method in your Product model
            
        })
    
    return JsonResponse({'products': results})





def Coupon1(request):
    coupon_code = 'WELCOME10'  # Adjust this if needed
    coupon = get_object_or_404(Coupon, code=coupon_code)
    return render(request, 'core/Coupon1.html', {'coupon': coupon})


def Coupon2(request):
    coupon_code = 'SEASON20'
    coupon = get_object_or_404(Coupon, code=coupon_code)
    return render(request, 'core/Coupon2.html', {'coupon': coupon})


def Coupon3(request):
    coupon_code = 'BUNDLE15'
    coupon = get_object_or_404(Coupon, code=coupon_code)
    return render(request, 'core/Coupon3.html', {'coupon': coupon})


def Deals(request):
    return render(request,'core/Deals.html')

def AboutUs(request):
    return render(request,'core/AboutUs.html')

@login_required
def Contact(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            messages.success(request, 'Your feedback has been recorded.')
            return redirect('Contact')  # Redirect to the contact page or another page
    else:
        form = ComplaintForm()
    
    contact_info = ContactInfo.objects.first()
    return render(request, 'core/Contact.html', {'form': form, 'contact_info': contact_info})



def Contact(request):
    # Fetch the contact info from the database
    contact_info = ContactInfo.objects.first()
    
    # If no contact info is found, provide default values
    if contact_info is None:
        contact_info = {
            'address': '123 Baker Street, London, UK',
            'phone': '+44 123 456 7890',
            'email': 'contact@swiftcart.com'
        }
    else:
        contact_info = {
            'address': contact_info.address,
            'phone': contact_info.phone,
            'email': contact_info.email
        }
    
    return render(request, 'core/Contact.html', {'contact_info': contact_info})

@login_required
def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            messages.success(request, 'Your complaint has been submitted successfully.')
            return redirect('Contact')
    else:
        form = ComplaintForm()
    return render(request, 'core/Contact.html', {'form': form})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if not created:  # If the item was not newly created, update the quantity
            cart_item.quantity = quantity  # Update quantity with the new value
        else:
            cart_item.quantity += quantity  # Add to the existing quantity
        cart_item.save()

    return redirect('view_cart')
@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'core/cart.html', {'cart_items': cart_items, 'total': total})

def checkout_placeholder(request):
    return render(request, 'core/checkout_placeholder.html')

@login_required
def remove_from_cart(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)
    return redirect('wishlist')

@login_required
def view_wishlist(request):
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
    return render(request, 'core/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    WishlistItem.objects.filter(wishlist=wishlist, product=product).delete()
    return redirect('wishlist')

@login_required
def create_payment_intent(request):
    total_price = request.GET.get('total_price', 0)  # Default to 0 if not provided
    return render(request, 'core/payment.html', {
        'total_price': total_price
    })



def confirm_payment(request):
    if request.method == 'POST':
        payment_intent_id = request.POST.get('payment_intent_id')
        try:
            intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            if intent.status == 'succeeded':
                # Handle successful payment here
                Order.objects.create(user=request.user, amount=100.00)
                return redirect('success_page')  # Redirect to success page
            else:
                # Handle failed payment here
                return redirect('failure_page')  # Redirect to failure page
        except stripe.error.StripeError:
            return redirect('failure_page')  # Redirect to failure page
        




def payment_page(request):
    total_price = request.GET.get('total_price', '0.00')
    return render(request, 'core/payment.html', {'total_price': total_price})

# Fake payment gateway response
FAKE_PAYMENT_GATEWAY_SUCCESS_CARD_NUMBER = '4111111111111111'




def calculate_total_price(user, coupon_code):
    # Dummy implementation for calculating the total price
    # Replace with actual calculation logic
    return 1030.00  # Example total price
def checkout(request):
    # Get the current user's cart items
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user=request.user)
    else:
        cart_items = CartItem.objects.none()
    
    # Additional logic and rendering
    return render(request, 'core/checkout_placeholder.html', {'cart_items': cart_items})




def finishing(request):
    return render(request, 'core/finishing.html')

def payment_failed(request):
    return render(request, 'core/payment_failed.html')

def process_payment(request):
    if request.method == 'POST':
        # Simulate processing the payment
        # For example, validate the payment method and redirect accordingly
        fake_card_number = '4242424242424242'
        user_card_number = request.POST.get('card_number')

        if user_card_number == fake_card_number:
            return redirect('finishing')
        else:
            return redirect('payment_failed')

    return HttpResponse("Invalid request method", status=405)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {'product': product})


@login_required
def process_checkout(request):
    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address')
        phone_number = request.POST.get('phone_number')
        coupon_code = request.POST.get('coupon')

        cart = get_object_or_404(Cart, user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        original_amount = sum(item.product.price * item.quantity for item in cart_items)

        # Apply coupon logic
        discount = Decimal('0')
        coupon_cost = Decimal('0')

        if coupon_code == 'coupon1':
            discount = Decimal('0.10')  # 10% discount
            coupon_cost = Decimal('10.00')
        elif coupon_code == 'coupon2':
            discount = Decimal('0.20')  # 20% discount
            coupon_cost = Decimal('15.00')
        elif coupon_code == 'coupon3':
            discount = Decimal('0.15')  # 15% discount
            coupon_cost = Decimal('7.00')

        final_amount = original_amount - (original_amount * discount) + coupon_cost

        # Save order details
        OrderDetail.objects.create(
            user=request.user,
            shipping_address=shipping_address,
            phone_number=phone_number,
            total_price=final_amount
        )

        return redirect(f'/payment/?total_price={final_amount:.2f}')

    return redirect('checkout')

def aboutus(request):
    return render(request, 'core/AboutUs.html')
