from venv import create
from django.urls import path
from kritiksaran_module.views import create_post
app_name = "kritiksaran_module"

urlpatterns = [
    path('', create_post, name="create_post"),
]