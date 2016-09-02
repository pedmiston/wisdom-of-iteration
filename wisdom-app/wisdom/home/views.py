from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def anchoring(request):
    return render(request, 'home_pages/anchoring.html')
