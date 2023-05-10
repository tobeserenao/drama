from django.urls import path

from .views import gpt_index_view, gpt_chat_completion_view

app_name = "gpt"
urlpatterns = [
    path("", gpt_index_view, name="index"),
    path('chat-completion/', gpt_chat_completion_view, name='chat-completion'),
]
