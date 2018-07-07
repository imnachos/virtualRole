from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.


class RaceCreateForm(forms.Form):
    race_name = forms.TextField(help_text="Enter a name for the class")

    def clean_race_name(self):
        cleaned_data = self.cleaned_data['race_name']

        # Remember to always return the cleaned data.
        return cleaned_data
