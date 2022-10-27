import datetime
from django.urls import reverse
from artikel.models import Post
from artikel.forms import PostForm
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def show_artikel(request):
  post = Post.objects.all()
  context = {
      # 'username': request.user.username,
      'post': post,
      'form': PostForm()
  }
  return render(request, "article_home.html", context)

def show_artikel_json(request):
  posts = Post.objects.all()
  return HttpResponse(serializers.serialize("json", posts), content_type="application/json")

def show_artikel_json_by_id(request, id):
  post = Post.objects.get(id=id)
  return HttpResponse(serializers.serialize("json", [post]), content_type="application/json")

def create_artikel(request):
  context = {
    'form': PostForm()
  }

  if request.method == "POST":
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      judul = post_form.cleaned_data["title"]
      deskripsi = post_form.cleaned_data["description"]
      image_url = post_form.cleaned_data["image_url"]
      Post.objects.create(title=judul, description=deskripsi, image_url=image_url, date=datetime.date.today())
      return HttpResponseRedirect(reverse("artikel:article_home"))
  return render(request, "create_article.html", context)

# update artikel
def update_artikel(request):
  if request.method == "POST":
    post_form = Post(request.POST)
    post = Post.objects.get(id=id)
    if post_form.is_valid():
      judul = post_form.cleaned_data["title"]
      deskripsi = post_form.cleaned_data["description"]
      image_url = post_form.cleaned_data["image_url"]

# delete artikel
@csrf_exempt
def delete_artikel(request, id):
  post = Post.objects.get(id=id)
  post.delete()
  return HttpResponse()
