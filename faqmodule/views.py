from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Faq

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
