from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)
from common.views import TitleMixin
from shop.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from shop.models import (Basket, Category, EmailVerification, Product,
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


class BasketListView(ListView):
    template_name = 'baskets.html'
    context_object_name = 'baskets'
    model = Basket

    def get_queryset(self):
        user = self.request.user
        return Basket.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = self.get_queryset()
        # Дополнительные данные, которые вы хотите добавить в контекст, можно добавить здесь
        return context


@login_required
def basket_add(request, product_id):
    Basket.create_or_update(product_id, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove_product(request, basket_id):
    basket = get_object_or_404(Basket, id=basket_id)

    # Уменьшаем количество товара в корзине
    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    else:
        # Если количество товара равно 1, удаляем товар из корзины
        basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


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
