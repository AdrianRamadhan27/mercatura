from django import forms

class PostForm(forms.Form):
  title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={"class":"inp-title", "placeholder": "Judul dari artikel"}))
  description = forms.CharField(label="Description", max_length=2000, widget=forms.Textarea(attrs={"class":"inp-description", "placeholder": "Isi dari artikel"}))
  image_url = forms.CharField(label="Image URL", max_length=200, widget=forms.Textarea(attrs={"class":"inp-img-url", "placeholder": "Tautan gambar pendukung isi artikel"}))