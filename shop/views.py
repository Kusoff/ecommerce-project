from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from .models import *
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from django.contrib.auth import logout


# Create your views here.
class HomeListView(ListView):
    model = Product
    template_name = 'home.html'
    paginate_by = 3  # пагинация происходит под капотом

    def get_queryset(self):
        queryset = super(HomeListView, self).get_queryset()  # тот же самый  product = Product.objects.all()
        category_id = self.kwargs.get('category_id')  # kwargs это входные данные в url в моем случае <id:category_id>
        return queryset.filter(
            category_id=category_id) if category_id else queryset  # queryset это сформированный список объектов, поэтому мы можем применить к нему фильтры
        # #здесь мы проверям, что если id_категории поступает, то мы фильтруем, если нет, то возвращаем список товаров

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeListView, self).get_context_data()
        context['title'] = 'Store - Каталог'
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    """Просмотр поста """
    model = Product
    slug_url_kwarg = 'product_slug'
    template_name = 'product.html'
    context_object_name = 'product'


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def cart_detail(request, total=0, counter=0, cart_items=None):
    products = Product.objects.all().filter(available=True)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))

        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter, products=products))


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')


def cart_remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')


class UserRegistrationView(CreateView):
    """Регистрация"""
    model = Users
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        context['title'] = 'Store - Регистрация'
        return context


class UserProfileView(UpdateView):
    model = Users
    form_class = UserProfileForm
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['title'] = 'Store - Личный кабинет'
        return context


class Login(LoginView):
    """Авторизация"""
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def signoutView(request):
    logout(request)
    return redirect('login')

# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('profile'))
#         else:
#             print(form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)
#     context = {
#         'title': 'Store - Профиль',
#         'form': form,
#         'cart': Cart.objects.filter(user=request.user),
#     }
#     return render(request, 'profile.html', context)
