import datetime
from django.urls import reverse
from artikel.models import Post
from artikel.forms import PostForm
from django.contrib import messages
from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# show all artikel
def show_artikel(request):
  post = Post.objects.all()
  context = {
    'post': post,
  }
  return render(request, "article_home.html", context)

# show artikel user
@login_required(login_url='/login/')
def show_artikel_user(request):
  context = {
    'username': request.user.username,
    'form': PostForm()
  }
  return render(request, "history_article.html", context)

# show artikel json
def show_artikel_json(request):
  posts = Post.objects.all()
  return HttpResponse(serializers.serialize("json", posts, use_natural_foreign_keys=True), content_type="application/json")

# show artikel json
@login_required(login_url='/auth/login/')
def show_artikel_json_filter(request):
  post = Post.objects.filter(author=request.user)
  return HttpResponse(serializers.serialize("json", post, use_natural_foreign_keys=True), content_type="application/json")

# show artikel json by id
def show_artikel_json_by_id(request, id):
  try:
    post = Post.objects.get(id=id)
    return HttpResponse(serializers.serialize("json", [post]), content_type="application/json")
  except:
    return HttpResponseNotFound(f"Article not exist (id: {id})")

# create artikel
@login_required(login_url='/login/')
def create_artikel(request):
  context = {
    'form': PostForm()
  }

  if request.method == "POST":
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      judul = request.POST.get("title")
      deskripsi = request.POST.get("description")
      image_url = request.POST.get("image_url")
      Post.objects.create(author=request.user, title=judul, description=deskripsi, image_url=image_url, date=datetime.date.today())
      return HttpResponse()
    return HttpResponseBadRequest()
  return render(request, "create_article.html", context)

@csrf_exempt
@login_required(login_url='/auth/login/')
def create_artikel_json(request):
  context = {
    'form': PostForm()
  }

  if request.method == "POST":
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      judul = request.POST.get("title")
      deskripsi = request.POST.get("description")
      image_url = request.POST.get("image_url")
      post = Post.objects.create(author=request.user, title=judul, description=deskripsi, image_url=image_url, date=datetime.date.today())
      
      response_data = {
            "status": True,
            "message": "Artikel berhasil dibuat!"
            # Insert any extra data if you want to pass data to Flutter
      }

      response_data['judul'] = judul
      response_data['deskripsi'] = deskripsi
      response_data['image_url'] = image_url
      response_data['id'] = post.id
      return JsonResponse(response_data, status=200)
    return JsonResponse({
            "status": False,
            "message": "Input tidak valid"
            # Insert any extra data if you want to pass data to Flutter
        }, status=401)
  return render(request, "create_article.html", context)

# update artikel
@login_required(login_url='/login/')
def update_artikel(request, id):
  try:
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      judul = request.POST.get("title")
      image_url = request.POST.get("image_url")
      deskripsi = request.POST.get("description")

      post = Post.objects.get(id=id)
      post.title = judul
      post.image_url = image_url
      post.description = deskripsi
      post.save()

      article = {
        'id': id,
        'title': post.title,
        'description': post.description,
        'image_url': post.image_url
      }
      
      data = {'article': article}
      return JsonResponse(data)
  except:
    return HttpResponseNotFound(f"Article not exist (id: {id})")

@csrf_exempt
@login_required(login_url='/auth/login/')
def update_artikel_json(request, id):
  try:
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      judul = request.POST.get("title")
      image_url = request.POST.get("image_url")
      deskripsi = request.POST.get("description")

      post = Post.objects.get(id=id)
      post.title = judul
      post.image_url = image_url
      post.description = deskripsi
      post.save()

      article = {
        'id': id,
        'title': post.title,
        'description': post.description,
        'image_url': post.image_url
      }
      
      data = {"article": article, "status": True,
            "message": "Artikel berhasil diubah"}
      return JsonResponse(data, status=200)
  except:
    data = {"status": False,
            "message": "Artikel tidak ditemukan"}
    return JsonResponse(data, status=401)

# delete artikel
@login_required(login_url='/login/')
@csrf_exempt
def delete_artikel(request, id):
  try:
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponse()
  except:
    return HttpResponseNotFound(f"Post not exist (id: {id})")

@login_required(login_url='/auth/login/')
@csrf_exempt
def delete_artikel_json(request, id):
  try:
    post = Post.objects.get(id=id)
    post.delete()
    return JsonResponse({
            "status": True,
            "message": "Post berhasil dihapus!"
            # Insert any extra data if you want to pass data to Flutter
        }, status=200)
  except:
    return JsonResponse({
            "status": False,
            "message": "Post tidak ditemukan!"
            # Insert any extra data if you want to pass data to Flutter
        }, status=401)

