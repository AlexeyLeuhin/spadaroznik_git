from django import forms
from .models import Publications


class PostForm(forms.Form):
    countries = forms.CharField(max_length=120)
    description = forms.CharField(widget=forms.Textarea)


    def save(self, commit=True):
        new_post = Publications.objects.create(countries=self.cleaned_data['countries'],
                                               description=self.cleaned_data['description'])
        return new_post
