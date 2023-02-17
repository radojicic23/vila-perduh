from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request, 'vikendica/index.html')

def contacts(request):
    return render(request, 'vikendica/contacts.html')

def features(request):
    return render(request, 'vikendica/features.html')

def about(request):
    return render(request, 'vikendica/about.html')
