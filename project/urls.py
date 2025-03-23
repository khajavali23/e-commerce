from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from core.views import (
    home, look1, sale, shoppage, wishlist,
    womenswear, get_products, base, cart_view, update_cart, add_to_cart,
    add_to_wishlist, remove_from_wishlist, user_login, logined_page,
    checkout, order_detail,productdetilspage,place_order, order_success

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
    path('cart/', cart_view, name='cart'),
    path('place-order/<int:order_id>/', place_order, name='place_order'),

    path('sale/<str:pk>/', sale, name='sale'),
    path('shoppage/', shoppage, name='shoppage'),
    path('wishlist/', wishlist, name='wishlist'),  # ✅ Removed duplicate
    path('womenswear/', womenswear, name='womenswear'),
    path('cart/', cart_view, name='cart'),
    path('api/products/', get_products, name='get_products'),
    path('base/', base, name='base'),
    path("update-cart/<int:item_id>/", update_cart, name="update-cart"),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path("add-to-wishlist/<int:product_id>/", add_to_wishlist, name="add_to_wishlist"),
    path('remove-from-wishlist/<int:item_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('checkout/', checkout, name='checkout'),
    path('order/<int:order_id>/', order_detail, name='order_detail'), 
    path('place-order/<int:order_id>/', place_order, name='place_order'),
    path('order-success/', order_success, name='order_success'), # ✅ Added missing order_detail URL
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
