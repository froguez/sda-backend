from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from products.models import Product
from products.forms import ContactForm
from django.urls import reverse_lazy
import random



def count_visited_view(request):
    num_visited = 0
    
    response = HttpResponse('You have visited this page %d times'%(num_visited))
    return response


def session_page_view(request):
    if not request.session.get('flavor'):
        print("I don't know what cookie this user likes!")
    else:
        print("His favorite flavor is " + request.session.get('flavor'))

    print(request.session)

    request.session['flavor']['choco'] = 3
    request.session['flavor']['vanilla'] = 10

    request.session.modified = True

    response = HttpResponse('Hello, world! Do you like cookies?')
    return response


def cookie_page_view(request):
    if not request.COOKIES.get('flavor'):
        print("I don't know what cookie this user likes!")
    else:
        print("His favorite flavor is " + request.COOKIES.get('flavor'))

    print(request.COOKIES)
    
    response = HttpResponse('Hello, world! Do you like cookies?')
    response.set_cookie('flavor', 'chocolate')
    return response


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

class DetailProductView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'

class UpdateProductView(UpdateView):
    model = Product
    template_name = 'update.html'
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('list')

class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('list')

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')


