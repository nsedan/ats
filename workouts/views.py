from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Workout, Category, WorkoutType, Review
from .forms import WorkoutForm, ReviewForm, CategoryForm, WorkoutTypeForm
from profiles.models import UserProfile
from checkout.models import OrderLineItem, Order


@login_required
def all_workouts(request):
    """ A view to return all workouts available for the current user """

    workouts = Workout.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    all_categories = Category.objects.all()
    all_types = WorkoutType.objects.all()
    current_categories = None
    current_types = None
    query = None
    sort = None
    direction = None

    user_workouts = []
    for order in orders:
        order = OrderLineItem.objects.all().filter(order=order).values_list('workout', flat=True)
        for o in list(order):
            user_workouts.append(str(o))

    if not request.user.is_superuser:
        for order in orders:
            order = get_object_or_404(OrderLineItem, order=order)
            item = order.workout.id
            workouts = workouts.exclude(id=item)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                workouts = workouts.annotate(lower_name=Lower('name'))

            # Allow to sort by category or type name instead of ID
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'workout_type':
                sortkey = 'workout_type__name'

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

        if 'workout_type' in request.GET:
            current_types = request.GET['workout_type'].split(',')
            workouts = workouts.filter(workout_type__name__in=current_types)
            current_types = WorkoutType.objects.filter(
                name__in=current_types)

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
        'all_types': all_types,
        'current_types': current_types,
        'current_sorting': current_sorting,
        'user_workouts': user_workouts,
    }

    return render(request, 'workouts/workouts.html', context)


@login_required
def workout_detail(request, workout_id):
    """ A view to return an specific workout """

    workout = get_object_or_404(Workout, pk=workout_id)
    reviews = Review.objects.all().filter(workout=workout_id)
    all_categories = Category.objects.all()
    all_types = WorkoutType.objects.all()
    user_can_review = False
    user_can_buy = True

    current_user = request.user.id
    try:
        profile = UserProfile.objects.get(user=current_user)
    except UserProfile.DoesNotExist:
        profile = None

    if profile is not None:
        orders = Order.objects.all().filter(user_profile=profile)
        for order in orders:
            order = OrderLineItem.objects.all().filter(order=order).values_list('workout', flat=True)
            for o in list(order):
                if workout_id == o:
                    user_can_buy = False
        review = Review.objects.all().filter(workout=workout, user=profile)
        if not review:
            user_can_review = True

    context = {
        'workout': workout,
        'reviews': reviews,
        'all_categories': all_categories,
        'all_types': all_types,
        'user_can_review': user_can_review,
        'user_can_buy': user_can_buy
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
    """ Delete a workout from the store.
        It's use is not recommended."""
    if not request.user.is_superuser:
        messages.error(request, 'You cannot do that!')
        return redirect(reverse('home'))

    workout = get_object_or_404(Workout, pk=workout_id)
    workout.delete()
    messages.success(request, 'Workout deleted!')
    return redirect(reverse('workouts'))


@login_required
def add_review(request, workout_id):
    """ Add a review to a workout """

    workout = get_object_or_404(Workout, pk=workout_id)
    current_user = request.user.id
    try:
        profile = UserProfile.objects.get(user=current_user)
    except UserProfile.DoesNotExist:
        profile = None
    if profile is not None:
        review = Review.objects.all().filter(workout=workout, user=profile)
    rating = workout.rating
    num_reviews = len(Review.objects.all().filter(workout=workout))

    if not review:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.save()
                user_rating = form.cleaned_data['rating']
                if num_reviews == 0:
                    Workout.objects.filter(pk=workout.id).update(rating=user_rating)
                else:
                    prev_acum_rating = rating * (num_reviews)
                    new_acum_rating = prev_acum_rating + user_rating
                    new_rating = new_acum_rating / (num_reviews+1)
                    Workout.objects.filter(pk=workout.id).update(rating=new_rating)

                messages.success(request, 'Successfully added review!')
                return redirect(reverse('workout_detail', args=[workout.id]))
            else:
                messages.error(
                    request, 'Failed to add review. Please ensure the form is valid.')
        else:
            form = ReviewForm(
                initial={"user": profile, "workout": workout})
    else:
        return redirect(reverse('workout_detail', args=[workout.id]))

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'workout': workout,
    }
    return render(request, template, context)


@login_required
def add_category(request):
    """ Add a category """
    if not request.user.is_superuser:
        messages.error(request, 'You cannot do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a category!')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Failed to add a category. Please ensure the form is valid.')
    else:
        form = CategoryForm()

    template = 'categories/add_category.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def add_workouttype(request):
    """ Add a workout type """
    if not request.user.is_superuser:
        messages.error(request, 'You cannot do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WorkoutTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added a workout type!')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Failed to add a workout type. Please ensure the form is valid.')
    else:
        form = WorkoutTypeForm()

    template = 'types/add_workouttype.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
