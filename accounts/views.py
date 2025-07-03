from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ContactMessageForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # after registration, go to login
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')


def home_view(request):
    return render(request, 'home.html')  # Ensure 'home.html' exists in templates

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def market_research(request):
    return render(request, 'market_research.html')

def contact(request):
    return render(request, 'contact.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted!")
            return redirect('submit_contact')
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})

# Simple Rule-Based Bot
def chatbot_response(message):
    message = message.lower()

    if "hello" in message:
        return "Hi there! How can I help you?"
    elif "your name" in message:
        return "I am DjangoBot!"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing great!"
    elif "bye" in message:
        return "Goodbye! Have a nice day!"
    elif "help" in message:
        return "Sure, I can assist you. Please type your query."
    else:
        fallback_responses = [
            "Hmm, interesting! Tell me more.",
            "I'm still learning. Can you ask differently?",
            "Sorry, I didn't get that. Try asking something else.",
            "That's a good question! Let me think...",
            "I'm not sure I understand. Can you rephrase?"
        ]
        return random.choice(fallback_responses)

def chatbot_view(request):
    return render(request, 'chatbot.html')

def get_response(request):
    user_message = request.GET.get('message')
    response = chatbot_response(user_message)
    return JsonResponse({'response': response})
