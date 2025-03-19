from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)  # Allow blank images
    is_subcategory = models.BooleanField(default=False)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        if self.parent_category:
            return f"{self.parent_category.name} → {self.name}"
        return self.name

# SubCategory Model (Linked to Category)



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

