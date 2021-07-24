import os
from os.path import join

from django import forms
from django.conf import settings

from interior_meet.designs.models import Design


class DesignForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = Design
        fields = ('title', 'type', 'city', 'country', 'description', 'image')
        labels = {
            'type': 'Type of project',
            'description': 'Short description',
            'image': 'Attach image',
        }


class CreateDesignForm(DesignForm):
    pass


class EditDesignForm(DesignForm):
    pass
    # def save(self, commit=True):
    #     db_design = Design.objects.get(pk=self.instance.id)
    #     if commit:
    #         os.remove(join(settings.MEDIA_ROOT, db_design.image.url[len('/media/designs/'):]))
    #     return super().save(commit)
    #
    # class Meta:
    #     model = Design
    #     fields = ('title', 'type', 'city', 'country', 'description', 'image')
    #     labels = {
    #         'type': 'Type of project',
    #         'description': 'Short description',
    #         'image': 'Attach image',
    #     }