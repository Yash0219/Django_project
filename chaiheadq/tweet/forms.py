from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    #meta class is madatory for ModelForm
    class Meta:
        model = Tweet
        fields = ['text', 'photo']