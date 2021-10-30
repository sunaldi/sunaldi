from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def article(request):
    return render(request, 'article.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

# https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models
