from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    home = 'home'
    context = {'home': home}
    return render(request, 'home.html', context)

