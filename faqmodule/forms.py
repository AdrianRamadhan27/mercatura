from django.forms import ModelForm
from django import forms
from faqmodule.models import Faq

class FaqCards(ModelForm):
    title = forms.CharField(max_length=255)
    description = forms.Textarea()
    class Meta:
        model = Faq
        fields = ['title','description']