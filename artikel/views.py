import datetime
from django.urls import reverse
from artikel.models import Post
from artikel.forms import PostForm
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# show all artikel
def show_artikel(request):
  post = Post.objects.all()
  context = {
      'username': request.user.username,
      'post': post,
      'form': PostForm()
  }
  return render(request, "article_home.html", context)

# show artikel user
@login_required(login_url='/login/')
def show_artikel_user(request):
  post = Post.objects.filter(author=request.user)
  print(post)
  context = {
      'username': request.user.username,
      'post': post,
      'form': PostForm()
  }
  return render(request, "history_article.html", context)

# show artikel json
def show_artikel_json(request):
  posts = Post.objects.all()
  return HttpResponse(serializers.serialize("json", posts, use_natural_foreign_keys=True), content_type="application/json")

# show artikel json
def show_artikel_json_filter(request):
  post = Post.objects.filter(author=request.user)
  return HttpResponse(serializers.serialize("json", post, use_natural_foreign_keys=True), content_type="application/json")


# show artikel json by id
def show_artikel_json_by_id(request, id):
  post = Post.objects.get(id=id)
  return HttpResponse(serializers.serialize("json", [post]), content_type="application/json")

# create artikel
@login_required(login_url='/login/')
def create_artikel(request):
  print(request.user)
  context = {
    'form': PostForm()
  }

  if request.method == "POST":
    post_form = PostForm(request.POST)
    if post_form.is_valid():
      judul = post_form.cleaned_data["title"]
      deskripsi = post_form.cleaned_data["description"]
      image_url = post_form.cleaned_data["image_url"]
      Post.objects.create(author=request.user, title=judul, description=deskripsi, image_url=image_url, date=datetime.date.today())
      print('halo')
      return HttpResponse()
    return HttpResponseBadRequest()
  return render(request, "create_article.html", context)

# update artikel
@login_required(login_url='/login/')
def update_artikel(request, id):
  post_form = PostForm(request.POST)
  if post_form.is_valid():
    judul = post_form.cleaned_data["title"]
    image_url = post_form.cleaned_data["image_url"]
    deskripsi = post_form.cleaned_data["description"]

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

# delete artikel
@login_required(login_url='/login/')
@csrf_exempt
def delete_artikel(request, id):
  post = Post.objects.get(id=id)
  post.delete()
  return HttpResponse()

