from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "form-control", "id": "title", "placeholder": "Topik kritik atau saran"
    }))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        "class":"form-control", "id": "description", "placeholder": "Deskripsi kritik atau saran"
    }))
    class Meta:
        model = Post
        fields = ['title', 'description',]