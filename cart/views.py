from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def remove_from_cart(request, item_id):
    """Remove the item from cart"""

    try:
        cart = request.session.get('cart', [])
        cart.remove(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception:
        return HttpResponse(status=500)
