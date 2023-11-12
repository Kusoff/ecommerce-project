from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)

from common.views import TitleMixin
from .utils import _cart_id
from shop.context_processors import cart_totals
from shop.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from shop.models import (Cart, CartItem, Category, EmailVerification, Product,
                         Users)


# Create your views here.
class HomeListView(TitleMixin, ListView):
    model = Product
    template_name = 'home.html'
    paginate_by = 3  # пагинация происходит под капотом
    title = 'Store'

    def get_queryset(self):
        queryset = super(HomeListView, self).get_queryset()  # тот же самый  product = Product.objects.all()
        category_id = self.kwargs.get('category_id')  # kwargs это входные данные в url в моем случае <id:category_id>
        return queryset.filter(
            category_id=category_id) if category_id else queryset  # queryset это сформированный список объектов,
        # поэтому мы можем применить к нему фильтры
        # #здесь мы проверям, что если id_категории поступает, то мы фильтруем, если нет, то возвращаем список товаров

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeListView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    """Просмотр поста """
    model = Product
    slug_url_kwarg = 'product_slug'
    template_name = 'product.html'
    context_object_name = 'product'


@login_required
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(user=request.user, cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user, cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()

    # После обновления корзины перенаправляем пользователя на предыдущую страницу
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def cart_detail(request):
    products = Product.objects.all().filter(available=True)

    # Использем контекст, предоставленный процессором cart_totals.
    context = cart_totals(request)

    # Добавляем к контексту товары.
    context['products'] = products

    # Используем контекст при рендеринге шаблона.
    return render(request, 'cart.html', context)


@login_required
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


@login_required
def cart_remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    """Регистрация"""
    model = Users
    form_class = UserRegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    success_message = 'Вы успешно зарегистрированы'
    title = 'Store - Регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = Users
    form_class = UserProfileForm
    template_name = 'profile.html'
    title = 'Store - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))


class UserLoginView(LoginView):
    """Авторизация"""
    form_class = UserLoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def signoutView(request):
    logout(request)
    return redirect('login')


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = Users.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('home'))
