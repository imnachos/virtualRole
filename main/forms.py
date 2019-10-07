from django import forms


class ActorEditForm(forms.Form):
    name = forms.CharField(required=False)
    surname = forms.CharField(required=False)
    description = forms.CharField(required=False)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        return cleaned_data

    def clean_surname(self):
        cleaned_data = self.cleaned_data['surname']

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        return cleaned_data