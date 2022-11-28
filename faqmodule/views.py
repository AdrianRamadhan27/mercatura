from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Faq
from .forms import FaqCards
from django.http import HttpResponse
from django.core import serializers

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

def show_faqforms_json(request):
  faqs = Faq.objects.all()
  return HttpResponse(serializers.serialize("json", faqs, use_natural_foreign_keys=True), content_type="application/json")