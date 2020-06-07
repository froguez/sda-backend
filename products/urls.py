from django.urls import path, include
from products.views import HomeView, products_list_view, HomeView2

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('home2/', HomeView2.as_view(), name='home2'),
    path('list/', products_list_view, name='list')
]
