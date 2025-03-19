from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product
from .models import Category
from .models import LookBook


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    search_fields = ('name', 'category')




admin.site.register(Category)



@admin.register(LookBook)
class LookBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Display these columns in the admin panel



