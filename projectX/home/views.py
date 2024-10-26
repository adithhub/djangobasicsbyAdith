from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    peoples = [
        {'name': 'Adith', 'age': 19},
        {'name': 'Ritvik', 'age': 32},
        {'name': 'Amal', 'age': 15},
        {'name': 'Akash', 'age': 12},
    ]
    return render(request, 'index.html', context={'peoples': peoples, 'page': 'Django-Index Page'})
def about(request):
    context = {'page':'About'}
    return render(request, 'about.html', context)
def contact(request):
    context = {'page':'Contact'}
    return render(request, 'contact.html', context)
def succcess_page(request):
    return HttpResponse("Hey this is success page.")
