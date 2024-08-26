# forms.py

from django import forms
from cards.models import Tasks, Cards

class CardTaskForm(forms.Form):
    tasks = forms.ModelMultipleChoiceField(
        queryset=Tasks.objects.none(),
        required=True,
        widget=forms.CheckboxSelectMultiple,
        label='Tareas Disponibles'
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CardTaskForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['tasks'].queryset = Tasks.objects.filter(user=user)
