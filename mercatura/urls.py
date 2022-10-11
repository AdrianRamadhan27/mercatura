from django.urls import path
from mercatura.views import show_home

application = "mercatura"

urlpatterns = [
    path('', show_home, name="show_home")
]