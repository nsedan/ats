from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = 'Remove'
    initial_text = 'Current Image'
    input_text = ''
    template_name = 'workouts/custom_widget_templates/custom_clearable_file_input.html'
