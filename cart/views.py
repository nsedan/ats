from django.shortcuts import render, redirect


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a workout to the shopping cart """

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', [])

    if item_id not in list(cart):
        cart.append(item_id)
    # else:
        # TODO: disable add to cart botton on frontend

    request.session['cart'] = cart
    return redirect(redirect_url)
