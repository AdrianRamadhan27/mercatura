from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Faq
from .forms import FaqCards
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
def show_faqforms(request):
    faqs = Faq.objects.all()
    form = FaqCards(request.POST or None)

    context = {
        'faqs': faqs,
        'form': form,
    }

    if request.method == 'POST' :
        title = request.POST.get('title')
        description = request.POST.get('description')

        faq = Faq.objects.create(
            title=title, 
            description=description,
            user=request.user
        )
        return redirect('faqmodule:show_faqforms')
    
    return render(request, "show_faq.html", context)

@csrf_exempt
def create_faq_json(request):
    form = FaqCards(request.POST or None)


    if request.method == 'POST':
        if form.is_valid():

            title = request.POST.get('title')
            description = request.POST.get('description')

            faq = Faq.objects.create(
                title=title, 
                description=description,
                user=request.user
            )

            response_data = {
                "status": True,
                "message": "Create FAQ Berhasil!"   
            }
            response_data['title'] = title
            response_data['description'] = description
            response_data['id'] = faq.id
            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Create FAQ Gagal!"
                # Insert any extra data if you want to pass data to Flutter
            }, status=401)

@login_required(login_url='/auth/login')
def show_faqforms_json(request):
  faqs = Faq.objects.all()
  return HttpResponse(serializers.serialize("json", faqs, use_natural_foreign_keys=True), content_type="application/json")