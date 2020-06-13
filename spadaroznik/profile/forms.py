from urllib import request
from django import forms
from django.core.files.images import get_image_dimensions

from spadaroznik.settings import BASE_DIR


class ProfileRedactForm(forms.Form):
    biography = forms.CharField(required=True)
    location = forms.CharField(required=True)
    birth_date = forms.DateField(required=False)
    avatar = forms.ImageField(required=False)

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        if avatar:
            w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 2080
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            # validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            # validate file size
            if len(avatar) > (4 * 1024 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')
        else:
            avatar = f'{BASE_DIR}\media\default.png'
        return avatar

    def save(self, user):
        user.profile.biography = self.cleaned_data['biography']
        user.profile.location = self.cleaned_data['location']
        user.profile.birth_date = self.cleaned_data['birth_date']
        user.profile.avatar = self.cleaned_data['avatar']
        user.profile.save()
