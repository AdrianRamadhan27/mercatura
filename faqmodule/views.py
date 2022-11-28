from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Faq
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
@login_required(login_url='/login')
def show_faqforms(request):
    title = Faq.objects.all()
    description = Faq.objects.all()
    context = {
        'title': title,
        'description': description,
    }
    
    return render(request, "show_faq.html", context)

def show_faqforms_json(request):
  faqs = Faq.objects.all()
  return HttpResponse(serializers.serialize("json", faqs, use_natural_foreign_keys=True), content_type="application/json")