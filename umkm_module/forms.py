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
    
    nama_usaha = forms.CharField(label="Nama Usaha", widget=forms.TextInput(attrs={"name": "nama_usaha", "class": "border-4"}))
    bidang_usaha = forms.CharField(label="Kuliner",widget=forms.RadioSelect(choices=BIDANG_USAHA, attrs={"name": "bidang_kuliner"}))
    deskripsi_usaha = forms.CharField(label="Deskripsi Usaha",widget=forms.Textarea(attrs={"name": "deskripsi_usaha", "class": "border-4"}))
    email_usaha = forms.EmailField(label="Email Usaha",widget=forms.EmailInput(attrs={"name": "email_usaha", "class": "border-4"}))
    lokasi_usaha = forms.CharField(label="Lokasi Usaha",widget=forms.Select(choices=PROVINSI,attrs={"name": "lokasi_usaha"}))
    website_usaha = forms.URLField(label="Website Usaha (Opsional)",widget=forms.URLInput(attrs={"name": "website_usaha", "class": "border-4"}), required=False)
    logo_usaha = forms.ImageField(label="Logo Usaha", widget=forms.FileInput(attrs={"name":"logo_usaha", "accept":"image/"}))
    # # create meta class
    class Meta:
        # specify model to be used
        model = UMKM
  
        # specify fields to be used
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UMKMForm, self).__init__(*args, **kwargs)
        self.fields['website_usaha'].required = False

class SearchForm(forms.Form):
    search_query = forms.CharField(label="Kata Kunci",widget=forms.TextInput(attrs={"name": "search_query", "class": "border-4"}), required=False)
    bidang_usaha = forms.CharField(label="Bidang", widget=forms.Select(choices=[("", "Bidang apapun")]+BIDANG_USAHA, attrs={"name": "bidang_usaha"}), required=False)
    lokasi_usaha = forms.CharField(label="Lokasi", widget=forms.Select(choices=[("", "Lokasi manapun")]+PROVINSI, attrs={"name": "lokasi_usaha"}), required=False)