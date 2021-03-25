from django.shortcuts import get_object_or_404
from workouts.models import Workout


def cart_contents(request):

    cart_items = []
    cart_ids = []
    total = 0
    cart = request.session.get('cart', [])

    for item_id in cart:
        workout = get_object_or_404(Workout, pk=item_id)
        total += workout.price
        cart_items.append(workout)
        cart_ids.append(item_id)

    context = {
        'cart_items': cart_items,
        'cart_ids': cart_ids,
        'total': total,
    }

    return context
