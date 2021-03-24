from django.contrib import admin
from .models import Workout, Category, WorkoutType, Review

# Register your models here.


class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'workout_type',
        'difficulty',
        'price',
        'rating',
        'is_deleted',
    )
    list_filter = (
        'category',
        'workout_type'
    )
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class WorkoutTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'workout',
        'rating',
        'created_at',
    )


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WorkoutType, WorkoutTypeAdmin)
admin.site.register(Review, ReviewAdmin)
