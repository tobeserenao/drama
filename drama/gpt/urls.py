from django.urls import path

from .views import gpt_index_view

app_name = "gpt"
urlpatterns = [
    path("", gpt_index_view, name="index"),
]
