from .models import Cart, CartItem, Category
from .utils import _cart_id


# функция которая возвращает количество товаров в корзине
def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Cart.DoesNotExist:
            item_count = 0
        return dict(item_count=item_count)

# функция которая возвращает все категории товаров
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)


def cart_totals(request):
    # Вызывает функцию calculate_totals для получения общей стоимости, количества товаров и списка товаров в корзине.
    total, counter, cart_items = calculate_totals(request)

    # Возвращает словарь с полученными значениями в контекст шаблона.
    return {'total': total, 'counter': counter, 'cart_items': cart_items}


def calculate_totals(request):
    # Инициализирует переменные для общей стоимости, количества товаров и списка товаров в корзине.
    total = 0
    counter = 0
    cart_items = []

    try:
        cart = Cart.objects.get(
            cart_id=_cart_id(request))  # Пытается получить объект корзины для текущего пользователя.
        cart_items = CartItem.objects.filter(cart=cart,
                                             active=True)  # Получает активные элементы корзины, связанные с корзиной.

        # Для каждого элемента корзины увеличивает общую стоимость и количество товаров.
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except Cart.DoesNotExist:
        # Обрабатывает случай, когда корзина не существует для текущего пользователя.
        pass
    return total, counter, cart_items  # Возвращает общую стоимость, количество товаров и список товаров в корзине.
