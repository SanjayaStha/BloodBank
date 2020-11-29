from django import forms

from .models import Blood

class CreateBlood(forms.ModelForm):
    class Meta:
        model = Blood
        fields = "__all__"