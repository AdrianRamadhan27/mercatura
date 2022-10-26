from django.shortcuts import render
from umkm_module.forms import UMKMForm
from django.shortcuts import redirect
from umkm_module.models import UMKM
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_umkm(request):
    return render(request, "umkm_list.html")



def show_json(request):
    umkm = UMKM.objects.all()
    return HttpResponse(serializers.serialize("json", umkm), content_type="application/json")

def detail_umkm(request, id):
    
    context = {
        'umkm': UMKM.objects.get(id = id)
    }

    return render(request, 'umkm_detail.html', context)


def tambah_umkm(request):
    form = UMKMForm(request.POST)
    if form.is_valid():
        umkm = form.save(commit=False)
        umkm.website_usaha = "https://www.google.com/search?q=" + str(umkm.nama_usaha)
        umkm.save()
        return redirect('umkm_module:show_umkm')

    context = {
        'form': form
    }
    return render(request, 'umkm_tambah.html', context)
