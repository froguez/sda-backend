from django.urls import path, include
from products.views import home_page_view, HomeView, product_list_view

urlpatterns = [
    path('', home_page_view),
    path('about/', HomeView.as_view()),
    path('list/', product_list_view),
]
