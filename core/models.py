from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models





class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)  # Regular category image
    banner_image = models.ImageField(upload_to='categories/banners/', blank=True, null=True)  # New banner image field
    is_subcategory = models.BooleanField(default=False)
    parent_category = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories'
    )

    def __str__(self):
        if self.parent_category:
            return f"{self.parent_category.name} → {self.name}"
        return self.name




# Product Model (Updated to include SubCategory)
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('printed_fabric', 'Printed Fabric'),
        ('solid_dyed_fabric', 'Solid Dyed Fabric'),
        ('fabric_set', 'Fabric Set'),
        ('dyed_fabric', 'Dyed Fabric'),
        ('shop_look', 'Shop Look'),
        ('womens_wear', "Women's Wear"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    # Main category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    # Subcategory (New field)

    # Images
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)
    hover_image = models.ImageField(upload_to='products/images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='products/images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='products/images/', blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LookBook(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)  # If it's an external link
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Allow nulls temporarily
    products = models.ManyToManyField(Product, through='CartItem') 


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)  
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def total_price(self):
        return self.quantity * self.product.price  

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"
    
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('online', 'Online Payment'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order_note = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cod')  # New field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username if self.user else 'Guest'} - {self.payment_method.upper()}"




class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Store price at the time of order

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"



class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name



