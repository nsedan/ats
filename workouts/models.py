from django.db import models
from taggit.managers import TaggableManager


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Workout(models.Model):
    diff_choices = (("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard"),)

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tags = TaggableManager()
    difficulty = models.CharField(max_length=12, choices=diff_choices)
    duration = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(max_length=1024, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
