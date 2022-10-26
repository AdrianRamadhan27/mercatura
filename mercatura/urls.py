from django.urls import path
from mercatura.views import show_home

app_name = "mercatura"

urlpatterns = [
    path('', show_home, name="show_home"),
]