from django.urls import path

from main.views import index, article, privacy, terms

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('article', article, name='article'),
    path('privacy', privacy, name='privacy'),
    path('terms', terms, name='terms'),
]
