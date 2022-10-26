from django import forms
from umkm_module.models import UMKM
  
  
# creating a form
class UMKMForm(forms.ModelForm):
    
    # create meta class
    class Meta:
        # specify model to be used
        model = UMKM
  
        # specify fields to be used
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UMKMForm, self).__init__(*args, **kwargs)
        self.fields['website_usaha'].required = False

