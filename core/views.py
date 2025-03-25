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
from .models import Order  


from django.conf import settings

def home(request):
    # Fetch required categories
    new_arrived_category = Category.objects.filter(name="New Arrived").first()
    japan_satin_fabric_category = Category.objects.filter(name="Japan Satin Fabric").first()
    trending_collection_category = Category.objects.filter(name="Trending Collection").first()
    fabric_set_category = Category.objects.filter(name="Fabric Set").first()
    plain_fabrics_category = Category.objects.filter(name="Plain Fabrics").first()
    featured_collection_category = Category.objects.filter(name="Featured Collection").first()
    patterned_fabric_category = Category.objects.filter(name="Patterned Fabric").first()
    best_seller_category = Category.objects.filter(name="Best Seller").first()
    pure_viscose_fabrics_category = Category.objects.filter(name="Pure & Viscose Fabrics").first()

    # Fetch products for the categories if they exist
    new_arrived_products = Product.objects.filter(category=new_arrived_category) if new_arrived_category else []
    japan_satin_fabric_products = Product.objects.filter(category=japan_satin_fabric_category) if japan_satin_fabric_category else []
    trending_collection_products = Product.objects.filter(category=trending_collection_category) if trending_collection_category else []
    fabric_set_products = Product.objects.filter(category=fabric_set_category) if fabric_set_category else []
    plain_fabrics_products = Product.objects.filter(category=plain_fabrics_category) if plain_fabrics_category else []
    featured_collection_products = Product.objects.filter(category=featured_collection_category) if featured_collection_category else []
    patterned_fabric_products = Product.objects.filter(category=patterned_fabric_category) if patterned_fabric_category else []
    best_seller_products = Product.objects.filter(category=best_seller_category) if best_seller_category else []
    pure_viscose_fabrics_products = Product.objects.filter(category=pure_viscose_fabrics_category) if pure_viscose_fabrics_category else []

    parent_categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

    context = {
        'new_arrived_products': new_arrived_products,
        'japan_satin_fabric_products': japan_satin_fabric_products,
        'trending_collection_products': trending_collection_products,
        'fabric_set_products': fabric_set_products,
        'plain_fabrics_products': plain_fabrics_products,
        'featured_collection_products': featured_collection_products,
        'patterned_fabric_products': patterned_fabric_products,
        'best_seller_products': best_seller_products,
        'pure_viscose_fabrics_products': pure_viscose_fabrics_products,
        'categories': parent_categories
    }
    
    return render(request, 'index.html', context)













from django.shortcuts import render, get_object_or_404
from .models import Category, Product  # Ensure correct model import

from django.shortcuts import render
from core.models import Category, Product
from django.shortcuts import render
from core.models import Category, Product

from django.shortcuts import render
from core.models import Category, Product
from django.shortcuts import render
from core.models import Category, Product

from django.shortcuts import render
from core.models import Category, Product

def home(request):
    # Fetch required categories
    new_arrived_category = Category.objects.filter(name="New Arrived").first()
    japan_satin_fabric_category = Category.objects.filter(name="Japan Satin Fabric").first()
    trending_collection_category = Category.objects.filter(name="Trending Collection").first()
    fabric_set_category = Category.objects.filter(name="Fabric Set").first()
    plain_fabrics_category = Category.objects.filter(name="Plain Fabrics").first()
    featured_collection_category = Category.objects.filter(name="Featured Collection").first()
    patterned_fabric_category = Category.objects.filter(name="Patterned Fabric").first()
    best_seller_category = Category.objects.filter(name="Best Seller").first()

    # Fetch products for the categories if they exist
    new_arrived_products = Product.objects.filter(category=new_arrived_category) if new_arrived_category else []
    japan_satin_fabric_products = Product.objects.filter(category=japan_satin_fabric_category) if japan_satin_fabric_category else []
    trending_collection_products = Product.objects.filter(category=trending_collection_category) if trending_collection_category else []
    fabric_set_products = Product.objects.filter(category=fabric_set_category) if fabric_set_category else []
    plain_fabrics_products = Product.objects.filter(category=plain_fabrics_category) if plain_fabrics_category else []
    featured_collection_products = Product.objects.filter(category=featured_collection_category) if featured_collection_category else []
    patterned_fabric_products = Product.objects.filter(category=patterned_fabric_category) if patterned_fabric_category else []
    best_seller_products = Product.objects.filter(category=best_seller_category) if best_seller_category else []

    parent_categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

    context = {
        'new_arrived_products': new_arrived_products,
        'japan_satin_fabric_products': japan_satin_fabric_products,
        'trending_collection_products': trending_collection_products,
        'fabric_set_products': fabric_set_products,
        'plain_fabrics_products': plain_fabrics_products,
        'featured_collection_products': featured_collection_products,
        'patterned_fabric_products': patterned_fabric_products,
        'best_seller_products': best_seller_products,
        'categories': parent_categories
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
    featured_collection_category = Category.objects.filter(name="Featured Collection").first()
    patterned_fabric_category = Category.objects.filter(name="Patterned Fabric").first()
    category = get_object_or_404(Category, id=pk)
    products = Product.objects.filter(category=category)
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')
    featured_collection_products = Product.objects.filter(category=featured_collection_category) if featured_collection_category else []
    patterned_fabric_products = Product.objects.filter(category=patterned_fabric_category) if patterned_fabric_category else []

    context = {
        'category': category,
        'products': products,
         'featured_collection_products': featured_collection_products,
        'patterned_fabric_products': patterned_fabric_products,
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


def newarrival_view(request):
    return render(request, 'newarrival.html')


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
    # Ensure user is authenticated
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to add items to the cart.")
        return redirect("login")  # Redirect to login page if not logged in

    product = get_object_or_404(Product, id=product_id)
    
    # Get or create a cart for the user
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # If the item already exists, increase the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} added to cart successfully!")

    # Redirect to cart page instead of rendering directly
    return redirect("cart_page")  # Ensure "cart_page" is defined in urls.py



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
    
    # Fetch Parent Categories
    parent_categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

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
        "total_price": order.total_price,
        "categories": parent_categories  # Ensure this is passed to the template
    })



def payment_success(request):
    return render(request, "payment_success.html")

def cart_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    cart = Cart.objects.filter(user=request.user).first()
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related("subcategories")
    cart_items = cart.cartitem_set.all() if cart else []

    context = {
        "categories": categories,
        "cart_items": cart_items,
    }

    return render(request, "cart.html", context)


def newarrival_view(request):  
    featured_collection_category = Category.objects.filter(name="Featured Collection").first()
    patterned_fabric_category = Category.objects.filter(name="Patterned Fabric").first()

    products = Product.objects.all()  
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

    featured_collection_products = Product.objects.filter(category=featured_collection_category) if featured_collection_category else []
    patterned_fabric_products = Product.objects.filter(category=patterned_fabric_category) if patterned_fabric_category else []

    context = {
        'products': products,
        'featured_collection_products': featured_collection_products,
        'patterned_fabric_products': patterned_fabric_products,
        'categories': categories
    }
    return render(request, 'newarrival.html', context)

def bestseller_view(request):
    featured_collection_category = Category.objects.filter(name="Featured Collection").first()
    patterned_fabric_category = Category.objects.filter(name="Patterned Fabric").first()

    products = Product.objects.all()  
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

    featured_collection_products = Product.objects.filter(category=featured_collection_category) if featured_collection_category else []
    patterned_fabric_products = Product.objects.filter(category=patterned_fabric_category) if patterned_fabric_category else []

    context = {
        'products': products,
        'featured_collection_products': featured_collection_products,
        'patterned_fabric_products': patterned_fabric_products,
        'categories': categories
    }
    return render(request, 'bestseller.html', context)