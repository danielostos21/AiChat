from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
import openai



openai_api_key = "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"
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        n = 1,
        stop = None,
        max_tokens = 500,
        temperature = 0.7,
    )   
    answer = response.choices[0].text.strip();
    return answer


# Create your views here.
def aichat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        
        response = ask_openai(message)
        return JsonResponse({ 'message': message, 'response': response})
    
    return render(request, 'chatbot.html')



def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST ['username']
        email = request.POST ['email']
        password1 = request.POST ['password1']
        password2 = request.POST ['password2']
        if password1 == password2:
            try:
                user = auth.models.User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return (redirect('chatbot'))
            except:
                error_message = 'Error creating account'
                    
        else:
            error_message = 'password dont match'
            return render(request, 'register.html', {'error_message': error_message})

    
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)