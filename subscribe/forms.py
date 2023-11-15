from django import forms
from .models import Subscriber

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('name', 'email',)

def __init__(self, *args, **kwargs):
        """add placeholders and classes """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email',
        }

        """autofocus and aria attributes"""
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['name'].widget.attrs['aria-label'] = 'Name'
        self.fields['email'].widget.attrs['aria-label'] = 'Email'
        
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black'
            self.fields[field].label = False