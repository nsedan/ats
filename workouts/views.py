from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Workout, Category
from .forms import WorkoutForm


@login_required
def all_workouts(request):
    """ A view to return all workouts """

    workouts = Workout.objects.all()
    all_categories = Category.objects.all()
    current_categories = None
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                workouts = workouts.annotate(lower_name=Lower('name'))

            # Allow to sort by category name instead of category ID
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            workouts = workouts.order_by(sortkey)

        if 'category' in request.GET:
            current_categories = request.GET['category'].split(',')
            workouts = workouts.filter(category__name__in=current_categories)
            current_categories = Category.objects.filter(
                name__in=current_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('workouts'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            workouts = workouts.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'workouts': workouts,
        'search_term': query,
        'all_categories': all_categories,
        'current_categories': current_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'workouts/workouts.html', context)


def workout_detail(request, workout_id):
    """ A view to return an specific workout """

    workout = get_object_or_404(Workout, pk=workout_id)
    all_categories = Category.objects.all()

    context = {
        'workout': workout,
        'all_categories': all_categories,
    }

    return render(request, 'workouts/workout_detail.html', context)


@login_required
def add_workout(request):
    """ Add a workout to the store """
    if not request.user.is_superuser:
        messages.error(request, 'You cannot do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WorkoutForm(request.POST, request.FILES)
        if form.is_valid():
            workout = form.save()
            messages.success(request, 'Successfully added workout!')
            return redirect(reverse('workout_detail', args=[workout.id]))
        else:
            messages.error(
                request, 'Failed to add workout. Please ensure the form is valid.')
    else:
        form = WorkoutForm()

    template = 'workouts/add_workout.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_workout(request, workout_id):
    """ Edit a workout in the store """
    if not request.user.is_superuser:
        messages.error(request, 'You cannot do that!')
        return redirect(reverse('home'))

    workout = get_object_or_404(Workout, pk=workout_id)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, request.FILES, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated workout!')
            return redirect(reverse('workout_detail', args=[workout.id]))
        else:
            messages.error(
                request, 'Failed to update workout. Please ensure the form is valid.')
    else:
        form = WorkoutForm(instance=workout)
        messages.info(request, f'You are editing {workout.name}')

    template = 'workouts/edit_workout.html'
    context = {
        'form': form,
        'workout': workout,
    }

    return render(request, template, context)


@login_required
def delete_workout(request, workout_id):
    """ Delete a workout from the store """
    if not request.user.is_superuser:
        messages.error(request, 'You cannot do that!')
        return redirect(reverse('home'))

    workout = get_object_or_404(Workout, pk=workout_id)
    workout.delete()
    messages.success(request, 'Workout deleted!')
    return redirect(reverse('workouts'))
