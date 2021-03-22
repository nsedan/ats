from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from profiles.models import UserProfile
from checkout.models import OrderLineItem


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a workout to the shopping cart """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    user_workouts = []
    for order in orders:
        order = get_object_or_404(OrderLineItem, order=order)
        item = order.workout.id
        user_workouts.append(str(item))

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', [])

    if item_id not in list(user_workouts):
        if item_id not in list(cart):
            cart.append(item_id)
            print(type(item_id))
        # else:
            # TODO: disable add to cart botton on frontend
            # message - item already in cart
    # else:
        # message - item already purchased

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
