from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class WorkoutType(models.Model):

    class Meta:
        verbose_name_plural = 'Workout Types'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Workout(models.Model):
    diff_choices = (("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard"),)

    name = models.CharField(max_length=254)
    description = models.TextField()
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)
    workout_type = models.ForeignKey(
        'WorkoutType', null=True, on_delete=models.SET_NULL)
    difficulty = models.CharField(max_length=12, choices=diff_choices)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=0)
    image = models.ImageField(blank=True)
    is_deleted = models.BooleanField(default=False, verbose_name='Inactive')

    def __str__(self):
        return self.name
