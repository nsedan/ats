from django.contrib import admin
from .models import Workout, Category, WorkoutType

# Register your models here.


class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'difficulty',
        'price',
        'rating',
        'is_deleted',
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


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WorkoutType, WorkoutTypeAdmin)
