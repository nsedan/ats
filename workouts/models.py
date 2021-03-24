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
    diff_choices = (("1", "Light"), ("2", "Easy"),
                    ("3", "Medium"), ("4", "Hard"), ("5", "Advanced"),)

    name = models.CharField(max_length=254)
    description = models.TextField()
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)
    workout_type = models.ForeignKey(
        'WorkoutType', null=True, on_delete=models.SET_NULL)
    difficulty = models.CharField(max_length=12, choices=diff_choices)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(blank=True, null=True, default=0)
    image = models.ImageField(blank=True)
    workout_program = models.ImageField(blank=True)
    is_deleted = models.BooleanField(default=False, verbose_name='Inactive')

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=255)
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE,
                                related_name='reviews',
                                related_query_name='review')
    user = models.ForeignKey('profiles.UserProfile', on_delete=models.CASCADE,
                             related_name='reviews',
                             related_query_name='review')
    rating = models.IntegerField(blank=True, null=True, default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
