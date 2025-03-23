from django.shortcuts import render, get_object_or_404, redirect 
from .models import Category, Product, LookBook, Cart, Order, OrderItem, Wishlist,CartItem
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required



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
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # If the item already exists, increase the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f"{product.name} added to cart successfully!")

    # Fetch all cart items after adding the product
    cart_items = cart.cartitem_set.all()

    return render(request, 'cart.html', {'cart_items': cart_items})

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
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        return redirect('cart')  

    total_price = sum(item.product.price * item.quantity for item in cart_items)

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
    return render(request, "order_detail.html", {"order": order})
