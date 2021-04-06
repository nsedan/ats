from django import forms

from .models import Workout, Category, WorkoutType, Review
from .widgets import CustomClearableFileInput


class WorkoutForm(forms.ModelForm):

    class Meta:
        model = Workout
        fields = '__all__'
        exclude = ('rating',)

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
    workout_program = forms.ImageField(
        label='Program', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        friendly_categories = [(c.id, c.get_friendly_name())
                               for c in categories]

        workout_types = WorkoutType.objects.all()
        friendly_types = [(c.id, c.get_friendly_name())
                          for c in workout_types]

        self.fields['category'].choices = friendly_categories
        self.fields['workout_type'].choices = friendly_types
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['workout'].widget = forms.HiddenInput()
        self.fields['rating'].widget.attrs['min'] = 0
        self.fields['rating'].widget.attrs['max'] = 10
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.HiddenInput()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'


class WorkoutTypeForm(forms.ModelForm):

    class Meta:
        model = WorkoutType
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.HiddenInput()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
