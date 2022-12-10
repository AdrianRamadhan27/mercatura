from django.shortcuts import render
from mercatura.models import Kisah
from mercatura.forms import FormKisah
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def show_home(request):
    kisah = Kisah.objects.all()
    # response_data = {}
    form = FormKisah(request.POST or None)

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        workfield = request.POST.get('workfield')
        description = request.POST.get('description')

        # response_data['name'] = name
        # response_data['age'] = age
        # response_data['workfield'] = workfield
        # response_data['description'] = description

        Kisah.objects.create(
            name = name,
            age = age,
            workfield = workfield,
            description = description,
        )
        return redirect('mercatura:show_home')
        # response_data['id'] = n.id
        # return JsonResponse(response_data)
    return render(request, 'home.html', {'kisah':kisah, 'form':form}) 

@csrf_exempt
def create_kisah_json(request):
    form = FormKisah(request.POST or None)

    if request.method == 'POST':
        if form.is_valid:
            name = request.POST.get('name')
            age = request.POST.get('age')
            workfield = request.POST.get('workfield')
            description = request.POST.get('description')


            kisah = Kisah.objects.create(
                name = name,
                age = age,
                workfield = workfield,
                description = description,
            )

            response_data = {
                "status": True,
                "message": "Create Kisah Berhasil!"
                # Insert any extra data if you want to pass data to Flutter
            }

            response_data['name'] = name
            response_data['age'] = age
            response_data['workfield'] = workfield
            response_data['description'] = description
            response_data['id'] = kisah.id

            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Create Kisah Gagal!"
                # Insert any extra data if you want to pass data to Flutter
            }, status=401)

def show_home_json(request):
  kisah = Kisah.objects.all()
  return HttpResponse(serializers.serialize("json", kisah, use_natural_foreign_keys=True), content_type="application/json")



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("mercatura:show_home")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password_one = request.POST.get('password1')
        password_two = request.POST.get('password2')
        username_ada = User.objects.filter(username=username).exists()
        if password_one == password_two and not username_ada:
            user = User.objects.create_user(username=username,password=password_two)
            if user is not None:
                user.save()
                return redirect('mercatura:login')
            else:
                messages.info(request,'Cek kembali password')
    return render(request,'register.html',{})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('mercatura:login'))
    response.delete_cookie('last_login')
    return response