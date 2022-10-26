from django.shortcuts import render

# Create your views here.
def show_umkm(request):
    return render(request, "umkm_list.html")