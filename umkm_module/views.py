from django.shortcuts import render
from umkm_module.forms import UMKMForm, SearchForm
from django.shortcuts import redirect
from umkm_module.models import UMKM
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
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





def search_umkm_json(request):
    if request.method == "POST":
        search_text = request.POST.get('search_query')
        bidang_usaha = request.POST.get('bidang_usaha')
        lokasi_usaha = request.POST.get('lokasi_usaha')
        umkms = UMKM.objects.filter(nama_usaha__icontains=search_text, bidang_usaha__icontains=bidang_usaha, lokasi_usaha__icontains=lokasi_usaha)
        return HttpResponse(serializers.serialize("json", umkms), content_type="application/json")


def detail_umkm(request, id):
    
    context = {
        'umkm': UMKM.objects.get(id = id)
    }

    return render(request, 'umkm_detail.html', context)

def detail_umkm_json(request, id):
    
    umkm = UMKM.objects.get(id=id)
    
    return HttpResponse(serializers.serialize("json", [umkm]), content_type="application/json")


@login_required(login_url='/login/')
def tambah_umkm(request):
    form = UMKMForm(request.POST)
    if request.method == 'POST':
        nama_usaha = request.POST.get('nama_usaha')
        bidang_usaha = request.POST.get('bidang_usaha')
        deskripsi_usaha = request.POST.get('deskripsi_usaha')
        lokasi_usaha = request.POST.get('lokasi_usaha')
        email_usaha = request.POST.get('email_usaha')
    
        website_usaha = request.POST.get('website_usaha')
        if website_usaha == '':
            website_usaha = "https://www.google.com/search?q=" + nama_usaha
        logo_usaha = request.POST.get('logo_usaha')

        UMKM.objects.create(
            nama_usaha=nama_usaha, 
            bidang_usaha=bidang_usaha,
            deskripsi_usaha=deskripsi_usaha,
            lokasi_usaha=lokasi_usaha,
            email_usaha=email_usaha,
            website_usaha=website_usaha,
            logo_usaha=logo_usaha,
            pemilik_usaha=request.user.username
        )
        return redirect('umkm_module:show_umkm')



    context = {
        'form': form
    }
    return render(request, 'umkm_tambah.html', context)

@csrf_exempt
@login_required(login_url='/auth/login/')
def tambah_umkm_json(request):
    if request.method == 'POST':
        nama_usaha = request.POST.get('nama_usaha')
        bidang_usaha = request.POST.get('bidang_usaha')
        deskripsi_usaha = request.POST.get('deskripsi_usaha')
        lokasi_usaha = request.POST.get('lokasi_usaha')
        email_usaha = request.POST.get('email_usaha')

        website_usaha = request.POST.get('website_usaha')
        if website_usaha == '':
            website_usaha = "https://www.google.com/search?q=" + nama_usaha
        
        pemilik_usaha = request.POST.get('pemilik_usaha')
        logo_usaha = request.POST.get('logo_usaha')
        umkm = UMKM.objects.create(
            nama_usaha=nama_usaha, 
            bidang_usaha=bidang_usaha,
            deskripsi_usaha=deskripsi_usaha,
            lokasi_usaha=lokasi_usaha,
            email_usaha=email_usaha,
            website_usaha=website_usaha,
            logo_usaha=logo_usaha,
            pemilik_usaha=pemilik_usaha
        )

        
        return JsonResponse({
            "status": True,
            "message": "Berhasil membuat usaha" + nama_usaha
        }, status=200)
    return JsonResponse({
            "status": False,
            "message": "Gagal membuat usaha"
        }, status=200)








@login_required(login_url='/login/')
def update_umkm(request, id):
    umkm_awal = UMKM.objects.get(id=id)
    form = UMKMForm(initial={
        'nama_usaha': umkm_awal.nama_usaha,
        'bidang_usaha': umkm_awal.bidang_usaha,
        'deskripsi_usaha': umkm_awal.deskripsi_usaha,
        'lokasi_usaha': umkm_awal.lokasi_usaha,
        'email_usaha': umkm_awal.email_usaha,
        'website_usaha': umkm_awal.website_usaha,
        'logo_usaha': umkm_awal.logo_usaha,
    })
    if request.user.username != umkm_awal.pemilik_usaha:
        return redirect('umkm_module:show_umkm')
    if request.method == 'POST':
        umkm_awal.nama_usaha = request.POST.get('nama_usaha')
        umkm_awal.bidang_usaha = request.POST.get('bidang_usaha')
        umkm_awal.deskripsi_usaha = request.POST.get('deskripsi_usaha')
        umkm_awal.lokasi_usaha = request.POST.get('lokasi_usaha')
        umkm_awal.email_usaha = request.POST.get('email_usaha')
    
        website_usaha = request.POST.get('website_usaha')
        if website_usaha == '':
            website_usaha = "https://www.google.com/search?q=" + umkm_awal.nama_usaha
        umkm_awal.website_usaha = website_usaha
        umkm_awal.logo_usaha = request.POST.get('logo_usaha')
        umkm_awal.save()
        
        return redirect('/umkm/detail/'+str(id))

    context = {
        'form': form
    }
    return render(request, 'umkm_update.html', context)

@csrf_exempt
@login_required(login_url='/auth/login/')
def update_umkm_json(request, id):
    umkm_awal = UMKM.objects.get(id=id)
    if request.user.username != umkm_awal.pemilik_usaha:
        return JsonResponse({
            "status": False,
            "message": "Anda bukan pemilik usaha"
        }, status=401)
    
    if request.method == 'POST':
        umkm_awal.nama_usaha = request.POST.get('nama_usaha')
        umkm_awal.bidang_usaha = request.POST.get('bidang_usaha')
        umkm_awal.deskripsi_usaha = request.POST.get('deskripsi_usaha')
        umkm_awal.lokasi_usaha = request.POST.get('lokasi_usaha')
        umkm_awal.email_usaha = request.POST.get('email_usaha')
    
        website_usaha = request.POST.get('website_usaha')
        if website_usaha == '':
            website_usaha = "https://www.google.com/search?q=" + umkm_awal.nama_usaha
        umkm_awal.website_usaha = website_usaha
        umkm_awal.logo_usaha = request.POST.get('logo_usaha')
        umkm_awal.save()
        response_data = {
            "status": True,
            "message": "Berhasil mengedit usaha"
        }

        response_data['nama_usaha'] = umkm_awal.nama_usaha
        response_data['bidang_usaha'] = umkm_awal.bidang_usaha
        response_data['deskripsi_usaha'] = umkm_awal.deskripsi_usaha
        response_data['lokasi_usaha'] = umkm_awal.lokasi_usaha
        response_data['email_usaha'] = umkm_awal.email_usaha
        response_data['website_usaha'] = umkm_awal.website_usaha
        response_data['logo_usaha'] = umkm_awal.logo_usaha
        response_data['id_usaha'] = umkm_awal.id
        return JsonResponse(response_data, status=200)


