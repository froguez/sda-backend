from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    context = {'context_text' : 'my simple page'}

    return render(request, 'index.html', context)

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context_text'] = 'my context text' 
        return context


def product_list_view(request):
    context = {'products':[
        {'pk': 1, 'name': 'Nintendo Switch', 'price': 350.0, 'category': 'Video Game'}
    ]}

    return render(request, 'list.html', context)
