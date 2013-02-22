from django import forms
from django.forms import ModelForm
from animals.models import Animals


class AnimalSelectionForm(forms.Form):
    choose_animal = forms.ModelChoiceField(
        queryset=Animals.objects.all(),
        required=False,
    )
    add_animal = forms.CharField(
        widget=forms.TextInput(
        ),
        required=False,
    )
