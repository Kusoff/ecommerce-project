# вынес эту функцию из views ProductDetailView чтобы устранить циклический импорт во views и context-processors
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
