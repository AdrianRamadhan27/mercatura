from venv import create
from django.urls import path
from django.urls import include, re_path
from kritiksaran_module.views import create_post, show_kritiksaran, setuju_post
app_name = "kritiksaran_module"

urlpatterns = [
    path('', create_post, name="create_post"),
    path('anon/', show_kritiksaran, name="show_kritiksaran"),
    path('setuju/', setuju_post, name="setuju-post-view"),

]