from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('category/<int:category_id>', views.HomeListView.as_view(), name='products_by_category'),
    path('page/<int:page>/', views.HomeListView.as_view(), name='paginator'),
    path('category/<int:category_id>/<slug:product_slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
    path('account/create/', views.UserRegistrationView.as_view(), name='signup'),
    path('account/login/', views.Login.as_view(), name='login'),
    path('account/signout/', views.signoutView, name='signout'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'), #UserProfileForm наследуется от класса UpdateView, который работает с конкреиным объектом, поэтому нужен его id


]