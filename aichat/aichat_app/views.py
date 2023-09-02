from django.shortcuts import render
from django.http import JsonResponse
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