from django.shortcuts import render, get_object_or_404, redirect 
from .models import Category, Product, LookBook, Cart, Order, OrderItem, Wishlist,CartItem,Subscriber
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import razorpay
from django.conf import settings


# Razorpay Client Object Create చేయండి
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Order  # Import your Order model


from django.conf import settings

# Razorpay Client Object Create చేయండి













def home(request):
    category = get_object_or_404(Category, name='Polyester Fabric')
    category_2 = get_object_or_404(Category, name='Japan Stain Fabr')
    
    
    japan_products = Product.objects.filter(category=category)
    japan_stain_fabr = Product.objects.filter(category=category_2)
    
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

    context = {
        'japan_products': japan_products,
        'japan_stain_fabr': japan_stain_fabr,
        'categories': categories
    }
    return render(request, 'index.html', context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Try again.")
            return redirect('login')

    return render(request, 'login.html')


@login_required
def logined_page(request):
    return render(request, 'logined.html')


def look1(request):
    look_books = LookBook.objects.all()
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

    context = {
        'look_books': look_books,
        'categories': categories
    }

    return render(request, 'look1.html', context)


def productdetilspage(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')
    
    context = {
        'product': product,
        'categories': categories
    }
    
    return render(request, 'productdetilspage.html', context)



def sale(request, pk):
    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category)
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

    context = {
        'category': category,
        'products': products,
        'categories': categories
    }

    return render(request, 'sale.html', context)


def shoppage(request):
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')
    return render(request, 'shoppage.html', {'categories': categories})


def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user) if request.user.is_authenticated else []
    subtotal = sum(item.product.price for item in wishlist_items)
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

    context = {
        'wishlist': wishlist_items,
        'subtotal': subtotal,
        'categories': categories
    }
    return render(request, "wishlist.html", context)


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        messages.info(request, "Product already in wishlist.")  # Use messages instead of print

    return redirect('wishlist')


def remove_from_wishlist(request, item_id):
    if request.method == "POST":
        wishlist_item = get_object_or_404(Wishlist, id=item_id, user=request.user)
        wishlist_item.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)


def womenswear(request):
    return render(request, 'womenswear.html')

@login_required
def move_to_cart(request, item_id):
    wishlist_item = get_object_or_404(Wishlist, id=item_id, user=request.user)
    product = wishlist_item.product

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the product already exists in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Increase quantity if it already exists
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # Remove the item from the wishlist
    wishlist_item.delete()

    messages.success(request, f"{product.name} moved to cart successfully!")

    return redirect('cart') 

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # If the item already exists, increase the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} added to cart successfully!")

    # Fetch all cart items after adding the product
    cart_items = cart.cartitem_set.all()

    # Merge the dictionaries
    context = {
        'categories': categories,
        'cart_items': cart_items  # Add cart items to the existing context
    }

    return render(request, 'cart.html', context)


@login_required
def update_cart(request, item_id):
    if request.method == "POST":
        new_quantity = request.POST.get("quantity")

        if not new_quantity or int(new_quantity) < 1:
            messages.error(request, "Invalid quantity.")
            return redirect("cart")

        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        cart_item.quantity = int(new_quantity)
        cart_item.save()

        messages.success(request, "Cart updated successfully!")
        return redirect("cart_view")

    return redirect("cart_view")

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()  # Get all items in the cart

    return render(request, 'cart.html', {'cart_items': cart_items})


def get_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def base(request):
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')
    return render(request, "base.html", {'categories': categories})


def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)  # Get the user's cart
    cart_items = CartItem.objects.filter(cart=cart)  # Get all cart items
    
    if not cart_items:
        return redirect('cart')  

    total_price = sum(item.product.price * item.quantity for item in cart_items)  # Calculate total

    order = Order.objects.create(user=request.user, total_price=total_price)

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()  # Clear the cart after checkout
    return redirect('order_detail', order_id=order.id)



def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

    # Merge the dictionaries
    context = {
        'categories': categories,
        'order': order  # Include order in the context
    }

    return render(request, "order_detail.html", context)


def place_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # Process order
        order.status = "Processing"
        order.save()
        
        return redirect('order_success')  # Ensure this matches `urls.py`

    return redirect('order_detail', order_id=order.id)

    return redirect('order_detail', order_id=order.id)
def order_success(request):
    return render(request, 'order_success.html')

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        country = request.POST.get("country")

        # Validate inputs
        if not email or not phone or not country:
            return JsonResponse({"success": False, "message": "All fields are required."}, status=400)

        # Save to the database
        subscriber, created = Subscriber.objects.get_or_create(email=email, defaults={"phone": phone, "country": country})

        if created:
            # Send confirmation email
            send_mail(
                "Welcome to Our Store!",
                "Thank you for subscribing! Use code SAVE10 for 10% off your first purchase.",
                "yourstore@example.com",  # Change this to your email
                [email],
                fail_silently=False,
            )
            messages.success(request, "Subscription successful! Check your email for the discount code.")
            return JsonResponse({"success": True, "message": "Subscription successful! Discount code sent."})
        else:
            return JsonResponse({"success": False, "message": "This email is already subscribed."}, status=400)
    
    return JsonResponse({"success": False, "message": "Invalid request."}, status=400)


def order_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    
    # Create Razorpay Order
    payment_data = {
        "amount": int(order.total_price * 100),  # Convert to paisa
        "currency": "INR",
        "payment_capture": 1
    }
    
    payment_order = client.order.create(data=payment_data)
    order.razorpay_order_id = payment_order['id']
    order.save()

    return render(request, "payment_page.html", {
        "order": order,
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "payment_order_id": payment_order['id'],
        "total_price": order.total_price
    })
def payment_success(request):
    return render(request, "payment_success.html")