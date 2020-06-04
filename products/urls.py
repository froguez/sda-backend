from django.urls import path, include
from products.views import home_page_view

urlpatterns = [
    path('', home_page_view)
]
