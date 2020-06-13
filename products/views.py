from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from products.models import Product
from django.urls import reverse_lazy
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

class ProductListView(ListView):
    model = Product
    template_name = 'list.html'
    context_object_name = 'products'

class CreateProductView(CreateView):
    model = Product
    template_name = 'create.html'
    fields = '__all__'
    success_url = reverse_lazy('list')

