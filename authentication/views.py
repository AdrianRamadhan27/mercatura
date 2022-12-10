from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        # Redirect to a success page.
        return JsonResponse({
            "status": True,
            "message": "Login Berhasil!"
            # Insert any extra data if you want to pass data to Flutter
        }, status=200)

    else:
        
        return JsonResponse({
            "status": False,
            "message": "Login Gagal, Username atau Password tidak Valid."
        }, status=401)

@csrf_exempt
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
                return JsonResponse({
                    "status": True,
                    "message": "Register Berhasil!"
                    # Insert any extra data if you want to pass data to Flutter
                }, status=200)

    return JsonResponse({
        "status": False,
        "message": "Register Gagal, username sudah dipakai."
    }, status=401)


def logout(request):
    auth_logout(request)
    return JsonResponse({
        "status": True,
        "message": "Logout Berhasil!"
        # Insert any extra data if you want to pass data to Flutter
    }, status=200)
