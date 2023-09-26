from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('page/<int:page_number>/', views.home, name='paginator'),
    path('category/<slug:category_slug>/', views.product, name='product_detail'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
    path('account/create/', views.Registration.as_view(), name='signup'),
    path('account/login/', views.Login.as_view(), name='login'),
    path('account/signout/', views.signoutView, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('test/', views.Test.as_view(), name='test'),
    path('category_chort/<slug:category_slug>/', views.Category.as_view(), name='category_chort'),
    path('product_chort/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_chort'),


]