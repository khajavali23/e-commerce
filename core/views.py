

from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    # Fetch the Category object for 'Polyester Fabric'
    category = get_object_or_404(Category, name='Polyester Fabric')
    
    # Now filter products by category instance
    japan_products = Product.objects.filter(category=category)
    
    # Fetch only main categories
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related('subcategories')

    context = {
        'japan_products': japan_products,
        'categories': categories
    }
    return render(request, 'index.html', context)



def login(request):
    return render(request, 'login.html')

def look1(request):
    look_books = LookBook.objects.all()  # Correct indentation
    return render(request, 'look1.html', {'look_books': look_books})  # Correct indentation



def productdetilspage(request):
    return render(request, 'productdetilspage.html')




def sale(request, pk):
    # Ensure 'category' is correctly fetched
    category = get_object_or_404(Category, id=pk)
    
    # Get products for this category
    products = Product.objects.filter(category=category)

    return render(request, 'sale.html', {'category': category, 'products': products})


def shoppage(request):
    return render(request, 'shoppage.html')

def  wishlist(request):
    return render(request, 'wishlist.html')

def womenswear(request):
    return render(request, 'womenswear.html')

def cart(request):
    return render(request, 'cart.html')

def get_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def base(request):
    return render(request, "base.html")

from django.shortcuts import render
from .models import LookBook

  # Fetch all Look Books from DB
   