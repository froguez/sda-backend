from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import random


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        lucky_number = random.randint(1, 100)

        context = {'messages': {'m1': 'Hello SDA!', 'm2': 'Im alive!'},
               'lucky_number': lucky_number}

        return context
    

class HomeView2(HomeView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        lucky_number = 7

        context = {'messages': {'m1': 'Hello SDA!', 'm2': 'Im dead!'},
                   'lucky_number': lucky_number}

        return context

def products_list_view(request):
    context = {'products' : [{'name' : 'xbox'}, {'name': 'Nintendo Switch'},
                            {'name': 'Ps4'}]
            }
    return render(request, 'list.html', context)
