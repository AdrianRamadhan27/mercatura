from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from django.shortcuts import redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def create_post(request):
    posts = Post.objects.all()
    response_data = {}
    form = PostForm()

    if request.POST.get('action') == 'post':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user

        response_data['title'] = title
        response_data['description'] = description
      
        Post.objects.create(
            title = title,
            description = description,
            # user = user,
            )
        return JsonResponse(response_data)

    return render(request, 'create_post.html', {'posts':posts, 'form':form}) 

def show_kritiksaran(request):
    posts = Post.objects.all()
    context={
        'posts':posts,
    }
    return render(request, "show_kritiksaran.html", context)