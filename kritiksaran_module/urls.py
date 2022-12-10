from django.urls import path
from django.urls import include, re_path
from kritiksaran_module.views import *


app_name = "kritiksaran_module"

urlpatterns = [
    path('', create_post, name="create_post"),
    path('create_post_json/', create_post_json, name="create_post_json"),
    path('anon/', show_kritiksaran, name="show_kritiksaran"),
    path('setuju/', setuju_post, name="setuju-post-view"),
    path('setuju_json/', setuju_post_json, name="setuju-post-json"),
    path('total/', total_number, name="total_number"),
    path('anon/total/', total_number_anon, name="total_number_anon"),
    path('json/', show_kritiksaran_json, name="show_kritiksaran_json"),


]