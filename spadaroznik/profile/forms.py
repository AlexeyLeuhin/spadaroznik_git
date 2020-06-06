from django import forms


class ProfileRedactForm(forms.Form):
    biography = forms.CharField(required=True)
    location = forms.CharField(required=True)
    birth_date = forms.DateField(required=False)
    #avatar = forms.ImageField(required=False)

    def save(self, user):
        user.profile.biography = self.cleaned_data['biography']
        user.profile.location = self.cleaned_data['location']
        user.profile.birth_date = self.cleaned_data['birth_date']
        #user.profile.avatar = self.cleaned_data['avatar']
        user.profile.save()
