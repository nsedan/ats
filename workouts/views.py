from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Workout


def all_workouts(request):
    """ A view to return all workouts """

    workouts = Workout.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('workouts'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            workouts = workouts.filter(queries)

    context = {
        'workouts': workouts,
        'search_term': query,
    }

    return render(request, 'workouts/workouts.html', context)


def workout_detail(request, workout_id):
    """ A view to return an specific workout """

    workout = get_object_or_404(Workout, pk=workout_id)

    context = {
        'workout': workout,
    }

    return render(request, 'workouts/workout_detail.html', context)
