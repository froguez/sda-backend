from django.urls import path, include
from products.views import HomeView, HomeView2, ProductListView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('home2/', HomeView2.as_view(), name='home2'),
    path('list/', ProductListView.as_view(), name='list')
]
