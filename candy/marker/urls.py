from django.urls import path
from .views import marker_view

app_name = "marker"

urlpatterns = [
    path("", marker_view, name="markers"),
]