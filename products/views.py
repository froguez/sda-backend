from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
    context = {'context_text' : 'my simple page'}

    return render(request, 'index.html', context)
