from django.shortcuts import render
from umkm_module.forms import UMKMForm, SearchForm
from django.shortcuts import redirect
from umkm_module.models import UMKM
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.files.storage import FileSystemStorage



# Create your views here.
def show_umkm(request):
    form = SearchForm(request.POST)
    return render(request, "umkm_list.html",{'form':form})

def search_umkm(request):
    if request.method == "POST":
        search_text = request.POST.get('search_query')
        bidang_usaha = request.POST.get('bidang_usaha')
        lokasi_usaha = request.POST.get('lokasi_usaha')
        umkms = UMKM.objects.filter(nama_usaha__icontains=search_text, bidang_usaha__icontains=bidang_usaha, lokasi_usaha__icontains=lokasi_usaha)
        return HttpResponse(serializers.serialize("json", umkms), content_type="application/json")
    return redirect('umkm_module:show_umkm') 

def show_json(request):
    
    umkms = UMKM.objects.all()
    return HttpResponse(serializers.serialize("json", umkms), content_type="application/json")


def detail_umkm(request, id):
    
    context = {
        'umkm': UMKM.objects.get(id = id)
    }

    return render(request, 'umkm_detail.html', context)


def tambah_umkm(request):
    form = UMKMForm(request.POST)
    if request.method == 'POST' and request.FILES['logo_usaha']:
        nama_usaha = request.POST.get('nama_usaha')
        bidang_usaha = request.POST.get('bidang_usaha')
        deskripsi_usaha = request.POST.get('deskripsi_usaha')
        lokasi_usaha = request.POST.get('lokasi_usaha')
        email_usaha = request.POST.get('email_usaha')
        if request.POST.get('website_usaha') is None:
            website_usaha = "https://www.google.com/search?q=" + nama_usaha
        else:
            website_usaha = request.POST.get('website_usaha')
        logo_upload = request.FILES['logo_usaha']
        fss = FileSystemStorage()
        file = fss.save(logo_upload.name, logo_upload)
        logo_usaha = fss.url(file)
        UMKM.objects.create(
            nama_usaha=nama_usaha, 
            bidang_usaha=bidang_usaha,
            deskripsi_usaha=deskripsi_usaha,
            lokasi_usaha=lokasi_usaha,
            email_usaha=email_usaha,
            website_usaha=website_usaha,
            logo_usaha=logo_usaha
        )
        return redirect('umkm_module:show_umkm')

    context = {
        'form': form
    }
    return render(request, 'umkm_tambah.html', context)

# def upload_image(request):
#     if request.method == 'POST' and request.FILES['upload']:
#         upload = request.FILES['upload']
#         fss = FileSystemStorage()
#         file = fss.save(upload.name, upload)
#         file_url = fss.url(file)
#         return render(request, 'umkm_tambah.html', {'file_url': file_url})
#     return render(request, 'umkm_tambah.html')