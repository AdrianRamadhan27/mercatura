from django.urls import path
from faqmodule.views import *

app_name = "faqmodule"

urlpatterns = [
    path('', show_faqforms, name="show_faqforms"),
    path('json/', show_faqforms_json, name="show_faqforms_json"),
    path('create_faq_json/', create_faq_json, name="create_faq_json"),

]