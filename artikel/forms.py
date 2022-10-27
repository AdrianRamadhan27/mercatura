from django import forms

class PostForm(forms.Form):
  title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={"class":"inp-title"}))
  description = forms.CharField(label="Description", max_length=2000, widget=forms.TextInput(attrs={"class":"inp-description"}))
  image_url = forms.CharField(label="Image URL", max_length=200, widget=forms.TextInput(attrs={"class":"inp-img-url"}))