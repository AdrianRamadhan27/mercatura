from django import forms
from umkm_module.models import UMKM

PROVINSI = [
  ('Aceh', 'Aceh' ),
  ('Sumatera Utara', 'Sumatera Utara' ),
  ('Sumatera', 'Sumatera' ), 
  ('Riau', 'Riau' ), 
  ('Jambi', 'Jambi' ),
  ('Sumatera Selatan', 'Sumatera Selatan' ), 
  ('Bengkulu', 'Bengkulu' ),
  ('Lampung', 'Lampung' ),
  ('Kepulauan Bangka Belitung', 'Kepulauan Bangka Belitung' ),
  ('Kepulauan Riau', 'Kepulauan Riau' ),
  ('DKI Jakarta', 'DKI Jakarta' ),
  ('Jawa Barat', 'Jawa Barat' ),
  ('Jawa Tengah', 'Jawa Tengah' ), 
  ('DI Yogyakarta', 'DI Yogyakarta' ), 
  ('Jawa Timur', 'Jawa Timur' ), 
  ('Banten', 'Banten' ),
  ('Bali', 'Bali' ), 
  ('Nusa Tenggara Barat', 'Nusa Tenggara Barat' ),
  ('Nusa Tenggara Timur', 'Nusa Tenggara Timur' ),
  ('Kalimantan Barat', 'Kalimantan Barat' ),
  ('Kalimantan Tengah', 'Kalimantan Tengah' ),  
  ('Kalimantan Selatan', 'Kalimantan Selatan' ),  
  ('Kalimantan Timur', 'Kalimantan Timur' ),  
  ('Kalimantan Utara', 'Kalimantan Utara' ),  
  ('Sulawesi Utara', 'Sulawesi Utara' ),  
  ('Sulawesi Tengah', 'Sulawesi Tengah' ),  
  ('Sulawesi Selatan', 'Sulawesi Selatan' ),  
  ('Sulawesi Tenggara', 'Sulawesi Tenggara' ),  
  ('Gorontalo', 'Gorontalo' ),
  ('Sulawesi Barat', 'Sulawesi Barat' ),  
  ('Maluku', 'Maluku' ),
  ('Maluku Utara', 'Maluku Utara' ),  
  ('Papua Barat', 'Papua Barat' ),  
  ('Papua', 'Papua' )
]

BIDANG_USAHA = [
    ('Kuliner', 'Kuliner'),
    ('Fashion', 'Fashion'),
    ('Agribisnis', 'Agribisnis')
]
  
# creating a form
class UMKMForm(forms.ModelForm):
    
    nama_usaha = forms.CharField(
        widget=forms.TextInput(attrs={
            "name": "nama_usaha",
            "id": "nama_usaha", 
            "class": "border border-2 p-2 rounded-md w-full",
            "required": "True"
            }),
            required=False)
    bidang_usaha = forms.CharField(
        widget=forms.RadioSelect(choices=BIDANG_USAHA, attrs={
            "name": "bidang_kuliner",
            "id": "bidang_kuliner",
            "required": "True"
            }))
    deskripsi_usaha = forms.CharField(
        widget=forms.Textarea(attrs={
            "name": "deskripsi_usaha",
            "id": "deskripsi_usaha", 
            "class": "border border-2 p-2 rounded-md w-full",
            "required": "True"
            }),
            required=False)
    email_usaha = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "name": "email_usaha",
            "id": "email_usaha", 
            "class": "border border-2 p-2 rounded-md w-full",
            "required": "True"
            }),
            required=False)
    lokasi_usaha = forms.CharField(
        widget=forms.Select(choices=PROVINSI,attrs={
            "name": "lokasi_usaha",
            "id": "lokasi_usaha",
            "class": "bg-gray-200 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            "required": "True"
            }),
            required=False)
    website_usaha = forms.URLField(
        widget=forms.URLInput(attrs={
            "name": "website_usaha",
            "id": "website_usaha", 
            "class": "border border-2 p-2 rounded-md w-full"
            }), 
            required=False)
    logo_usaha = forms.ImageField(
        widget=forms.FileInput(attrs={
            "name": "logo_usaha",
            "id": "logo_usaha", 
            "accept":"image/",
            "required": "True"
            }),
            required=False)
    # # create meta class
    class Meta:
        # specify model to be used
        model = UMKM
  
        # specify fields to be used
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UMKMForm, self).__init__(*args, **kwargs)
        self.fields['website_usaha'].required = False
        self.label_suffix = ""
         
        for field in self.fields.values():
            field.error_messages = {'required':''}
            

class SearchForm(forms.Form):
    search_query = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "name": "search_query", 
                "class": "font-poppins p-2 rounded-sm border border-2 w-full", 
                "placeholder": "Masukkan kata kunci"}), 
        required=False)
    bidang_usaha = forms.CharField(
        label="", 
        widget=forms.Select(
            choices=[("", "Semua Bidang")]+BIDANG_USAHA, 
            attrs={
                "name": "bidang_usaha", 
                "class": "font-poppins bg-gray-200 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                }), 
                required=False)
    lokasi_usaha = forms.CharField(label="", 
        widget=forms.Select(choices=[("", "Semua Lokasi")]+PROVINSI, 
        attrs={
            "name": "lokasi_usaha",
            "class": "font-poppins bg-gray-200 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
            }), 
        required=False)