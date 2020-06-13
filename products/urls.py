from django.urls import path, include
from products.views import HomeView, HomeView2, ProductListView, CreateProductView, UpdateProductView, DeleteProductView, DetailProductView, ContactView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('home/', HomeView.as_view(), name='home'),
    path('home2/', HomeView2.as_view(), name='home2'),
    path('list/', ProductListView.as_view(), name='list'),
    path('create/', CreateProductView.as_view(), name='create'),
    path('detail/<int:pk>', DetailProductView.as_view(), name='detail'),
    path('update/<int:pk>', UpdateProductView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete')
]
