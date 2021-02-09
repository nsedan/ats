from django.shortcuts import render, get_object_or_404
from .models import Workout


def all_workouts(request):
    """ A view to return all workouts """

    workouts = Workout.objects.all()

    context = {
        'workouts': workouts,
    }

    return render(request, 'workouts/workouts.html', context)


def workout_detail(request, workout_id):
    """ A view to return an specific workout """

    workout = get_object_or_404(Workout, pk=workout_id)

    context = {
        'workout': workout,
    }

    return render(request, 'workouts/workout_detail.html', context)
