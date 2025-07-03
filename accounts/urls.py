from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('contact/', views.contact_view, name='submit_contact'),
    path('', views.chatbot_view, name='chatbot'),
    path('get-response/', views.get_response, name='get_response'),
]   