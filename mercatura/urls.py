from django.urls import path
from mercatura.views import *

app_name = "mercatura"

urlpatterns = [
    path('', show_home, name="show_home"),
    path('create_kisah_json/', create_kisah_json, name='create_kisah_json'),
    path('json/', show_home_json, name="show_home_json"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]