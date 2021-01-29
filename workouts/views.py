from django.shortcuts import render
from .models import Workout


def all_workouts(request):
    """ A view to return all workouts """

    workouts = Workout.objects.all()

    context = {
        'workouts': workouts,
    }

    return render(request, 'workouts/workouts.html', context)
