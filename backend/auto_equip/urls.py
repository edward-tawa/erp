"""
URL configuration for auto_equip project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls.user_urls")),
    path("api/inventory/categories/", include("inventory.urls.category_urls")),
    path("api/inventory/products/", include("inventory.urls.product_urls")),
    path("api/inventory/product-stocks/", include("inventory.urls.product_stock_urls")),
    path("api/inventory/stock-movements/", include("inventory.urls.stock_movement_urls")),
    path("api/inventory/stock-takes/", include("inventory.urls.stock_take_urls")),
    path("api/inventory/stock-take-items/", include("inventory.urls.stock_take_item_urls")),
    path("api/sales/customers/", include("sales.urls.customer_urls")),
    path("api/sales/sales-orders/", include("sales.urls.sales_order_urls")),
    path("api/sales/sales-order-items/", include("sales.urls.sales_order_item_urls")),
    path("api/sales/carts/", include("sales.urls.cart_urls")),
    path("api/sales/cart-items/", include("sales.urls.cart_item_urls")),
    path("api/sales/payments/", include("sales.urls.payment_urls")),
    path("api/sales/receipts/", include("sales.urls.receipt_urls")),
    path("api/sales/receipt-items/", include("sales.urls.receipt_item_urls")),
    path("api/sales/sales/", include("sales.urls.sale_urls")),
    path("api/auth/", include("authentication.urls.auth_urls")),
]
