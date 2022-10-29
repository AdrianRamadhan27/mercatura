from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.
def show_home(request):
    return render(request, "home.html")

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