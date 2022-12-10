from ssl import _create_default_https_context
from django.shortcuts import render
from django.http import JsonResponse
from .models import Post, Setuju
from django.shortcuts import redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt



# @login_required(login_url='/login')
@csrf_exempt
def create_post(request):

    posts = Post.objects.all()
    response_data = {}
    form = PostForm()
    user = request.user

    if request.POST.get('action') == 'post':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        username = request.user.username
        setuju = 0

        response_data['title'] = title
        response_data['description'] = description
        response_data['username'] = username
        response_data['setuju'] = setuju

        n = Post.objects.create(
            title = title,
            description = description,
            user = user,
            username = username,
            )
        response_data['id'] = n.id
        response_data['total-setuju']= n.setuju.all().count()
        return JsonResponse(response_data)

    return render(request, 'create_post.html', {'posts':posts, 'form':form,}) 

@csrf_exempt
def create_post_json(request):
    
    form = PostForm(request.POST)
    user = request.user

    if request.method == 'POST':
        if form.is_valid():
            response_data = {
                "status": True,
                "message": "Kritik/Saran berhasil dibuat!"
            }
            title = request.POST.get('title')
            description = request.POST.get('description')
            user = request.user
            username = request.user.username
            setuju = 0

            response_data['title'] = title
            response_data['description'] = description
            response_data['username'] = username
            response_data['setuju'] = setuju

            n = Post.objects.create(
                title = title,
                description = description,
                user = user,
                username = username,
                )
            response_data['id'] = n.id
            response_data['total-setuju']= n.setuju.all().count()
            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Input tidak valid"
            }, status=401)


def show_kritiksaran(request):
    posts = Post.objects.all()
    context={
        'posts':posts,
    }
    return render(request, "show_kritiksaran.html", context)

def show_kritiksaran_json(request):
  posts = Post.objects.all()
  return HttpResponse(serializers.serialize("json", posts, use_natural_foreign_keys=True), content_type="application/json")

@login_required(login_url='/login')
def setuju_post(request):
    user = request.user
    if request.method == 'POST':
        post_obj = get_object_or_404(Post, id=request.POST.get('post_id'))
        post_id = post_obj.id
        user = request.user

        if user not in post_obj.setuju.all():
            post_obj.setuju.add(user)

        setuju, created = Setuju.objects.get_or_create(user=user, post_id=post_id)

        if created:

            post_obj.save()
            setuju.save()
    return redirect('kritiksaran_module:create_post')

@login_required(login_url='/login')
def setuju_post_json(request):
    user = request.user
    if request.method == 'POST':
        post_obj = get_object_or_404(Post, id=request.POST.get('post_id'))
        post_id = post_obj.id
        user = request.user

        if user not in post_obj.setuju.all():
            post_obj.setuju.add(user)

        setuju, created = Setuju.objects.get_or_create(user=user, post_id=post_id)

        if created:
            post_obj.save()
            setuju.save()

    return JsonResponse({
        "status": True,
        "message": "Setuju Berhasil!"
        # Insert any extra data if you want to pass data to Flutter
    }, status=200)


def total_number(request):
    if request.method == 'GET':
        post_obj = Post.objects.all().count()
        return HttpResponse(post_obj)
    return redirect('kritiksaran_module:create_post')


def total_number_anon(request):
    if request.method == 'GET':
        post_obj = Post.objects.all().count()
        return HttpResponse(post_obj)
    return redirect('kritiksaran_module:show_kritiksaran')




