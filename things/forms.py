"""Forms of the project."""

# Create your forms here.

from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity'] #excluding created_at for now
    