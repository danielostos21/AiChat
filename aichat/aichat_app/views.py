from django.shortcuts import render

# Create your views here.
def aichat(request):
    return render(request, 'chatbot.html')