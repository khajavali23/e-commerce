from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from core.views import (
    home, look1, sale, shoppage, wishlist,
    womenswear, get_products, base, cart_view, update_cart, add_to_cart,
    add_to_wishlist, remove_from_wishlist, user_login, logined_page,
    checkout, order_detail, productdetilspage, place_order, order_success,
    move_to_cart, subscribe, order_payment, payment_success, newarrival_view,
    bestseller_view, admin_dashboard
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('logined/', logined_page, name='logined'),
    path('look1/', look1, name='look1'),
    path('product/<int:product_id>/', productdetilspage, name='productdetilspage'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_page'),
    path('place-order/<int:order_id>/', place_order, name='place_order'),
    path('move-to-cart/<int:item_id>/', move_to_cart, name='move_to_cart'),
    path('subscribe/', subscribe, name='subscribe'),
    path('order/<int:order_id>/payment/', order_payment, name='order_payment'),
    path('success/', payment_success, name='payment_success'),
    path('sale/<str:pk>/', sale, name='sale'),
    path('shoppage/', shoppage, name='shoppage'),
    path('wishlist/', wishlist, name='wishlist'),
    path('womenswear/', womenswear, name='womenswear'),
    path('api/products/', get_products, name='get_products'),
    path('base/', base, name='base'),
    path('update-cart/<int:item_id>/', update_cart, name='update-cart'),
    path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:item_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('checkout/', checkout, name='checkout'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('order-success/', order_success, name='order_success'),
    path('newarrival/', newarrival_view, name='newarrival'),
    path('bestseller/', bestseller_view, name='bestseller'),
    path('admin_dashboard/', admin_dashboard, name='admin-dashboard'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)