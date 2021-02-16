from django.shortcuts import get_object_or_404
from workouts.models import Workout


def cart_contents(request):

    cart_items = []
    total = 0
    cart = request.session.get('cart', [])

    for item_id in cart:
        workout = get_object_or_404(Workout, pk=item_id)
        total += workout.price
        cart_items.append({
            'item_id': item_id,
            'workout': workout,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
    }

    return context
