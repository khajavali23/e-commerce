"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, login, look1, productdetilspage, sale, shoppage, wishlist, womenswear, cart, get_products, base
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login', login, name='login'),
    path('look', look1,name='look'),
    path('productdetilspage', productdetilspage, name='productdetilspage'),
    path('sale/<str:pk>/', sale, name='sale'),
    path('shoppage', shoppage,name='shoppage'),
    path('wishlist', wishlist, name='wishlist'),
    path('womenswear', womenswear, name='womenswear'),
    path('cart', cart, name='cart'),
    path('api/products/', get_products, name='get_products'),
    path('base',base,name='base')

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


