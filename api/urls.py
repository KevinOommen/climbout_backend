# boilerplate code for urls

from django.urls import path
from . import views

urlpatterns = [
    path('chatbot_response', views.chatgpt_response, name='chatgpt_response'),

]
