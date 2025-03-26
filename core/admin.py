from django.contrib import admin
from .models import Category, Product, LookBook, Cart, Wishlist, Order, OrderItem 
from django.urls import reverse
from django.utils.html import format_html
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





admin.site.site_header = "Fab Vogue Studio Admin"
admin.site.site_title = "Fab Vogue Dashboard"
admin.site.index_title = "Welcome to Fab Vogue Admin Panel"

def dashboard_link(obj):
    return format_html('<a href="{}" style="color: blue; font-weight: bold;">Go to Dashboard</a>', reverse('admin-dashboard'))

dashboard_link.short_description = "Custom Dashboard"
admin.site.add_action(dashboard_link)