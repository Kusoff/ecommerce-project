from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('category/<int:category_id>', views.HomeListView.as_view(), name='products_by_category'),
    path('page/<int:page>/', views.HomeListView.as_view(), name='paginator'),
    path('category/<int:category_id>/<slug:product_slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('baskets/', login_required(views.BasketListView.as_view()), name='basket_list'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
    path('baskets/remove_product/<int:basket_id>/', views.basket_remove_product, name='basket_remove_product'),
    path('account/create/', views.UserRegistrationView.as_view(), name='signup'),
    path('account/login/', views.UserLoginView.as_view(), name='login'),
    path('account/signout/', views.signoutView, name='signout'),
    path('profile/<int:pk>/', login_required(views.UserProfileView.as_view()), name='profile'),
    # UserProfileForm наследуется от класса UpdateView, который работает с конкреиным объектом, поэтому нужен его id
    path('verify/<str:email>/<uuid:code>/', views.EmailVerificationView.as_view(), name='email_verification'),

]
