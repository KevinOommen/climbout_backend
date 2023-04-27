# boilerplate code for urls

from django.urls import path
from . import views

urlpatterns = [
    path('chatbot_response', views.chatbot_response, name='chatbot_response'),
    path('add_event', views.add_event.as_view(), name='add_event'),
    path('chatbot_query', views.chatbot_query, name='chatbot_query'),
]
