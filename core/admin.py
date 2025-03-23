from django.contrib import admin
from .models import Category, Product, LookBook, Cart, Wishlist, Order, OrderItem 

# ✅ Proper way to register Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category')  # Customize fields as needed

# ✅ Register other models normally
admin.site.register(Product)
admin.site.register(LookBook)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)


