from django.contrib import admin
from .models import Workout, Category

# Register your models here.


class WorkoutAdmin(admin.ModelAdmin):
    """
    docstring
    """
    list_display = (
        'name',
        'category',
        'difficulty',
        'price',
        'duration',
        'rating'
    )
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    docstring
    """
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Category, CategoryAdmin)
