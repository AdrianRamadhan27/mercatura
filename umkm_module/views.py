from django.shortcuts import render
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