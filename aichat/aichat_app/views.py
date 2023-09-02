from django.shortcuts import render
from django.http import JsonResponse
import openai

openai_api_key = "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"
openai.api_key = openai_api_key

# def ask_openai(message):
#     response = openai.ChatCompletion.create(
#         model = "text-davinci-003",
#         prommt = message,
#         n = 1,
#         stop = None,
#         max_tokens = 150,
#         temperature = 0.7,
#     )   
#     print(response)
#     answer = response.choices[0].text.strip();
#     return answer

# Create your views here.
def aichat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
       
        response = "Hola"
        return JsonResponse({ 'message': message, 'response': response})
    
    return render(request, 'chatbot.html')