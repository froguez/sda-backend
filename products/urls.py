from django.urls import path, include
from products.views import HomeView, HomeView2, ProductListView
from products.views import CreateProductView, UpdateProductView
from products.views import DeleteProductView, DetailProductView, ContactView
from products.views import cookie_page_view, session_page_view, count_visited_view

urlpatterns = [
    path('count/', count_visited_view),
    path('cookie/', cookie_page_view),
    path('session/', session_page_view),
    path('contact/', ContactView.as_view(), name='contact'),
    path('home/', HomeView.as_view(), name='home'),
    path('home2/', HomeView2.as_view(), name='home2'),
    path('list/', ProductListView.as_view(), name='list'),
    path('create/', CreateProductView.as_view(), name='create'),
    path('detail/<int:pk>', DetailProductView.as_view(), name='detail'),
    path('update/<int:pk>', UpdateProductView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteProductView.as_view(), name='delete')
]
