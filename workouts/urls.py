from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_workouts, name='workouts'),
    path('<int:workout_id>/', views.workout_detail, name='workout_detail'),
    path('add/', views.add_workout, name='add_workout'),
]
