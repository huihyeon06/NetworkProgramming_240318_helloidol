from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World")

def say_hello_html(request):
    return render(request, 'playground/hello.html', {'name': '야', 'greeting': 'hi'})

def bye_html(request):
    context = {
        'singer':'박재정',
        'title':'헤어지자 말해요'
    }
    return render(request, 'playground/bye.html', context=context)


