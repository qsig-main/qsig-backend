from django import forms

from .models import Pitch

class PitchForm(forms.ModelForm):
    class Meta:
        model = Pitch
        fields = [
            # 'user',
            'title',
            'description',
            'date_created',
        ]