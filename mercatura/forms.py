from django import forms
from .models import Kisah

class FormKisah(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control", "id": "name", "placeholder": "Nama anda"
    }))
    age = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "form-control", "id": "age", "placeholder": "Usia anda"
    }))
    workfield = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control", "id": "workfield", "placeholder": "Bidang Pekerjaan yang anda kisahkan"
    }))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        "class":"form-control", "id": "description", "placeholder": "Deskripsi dari kisah"
    }))
    class Meta:
        model = Kisah
        fields = ['name', 'age', 'workfield', 'description',]