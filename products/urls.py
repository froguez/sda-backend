from django.urls import path, include
from products.views import home_page_view, HomeView

urlpatterns = [
    path('', home_page_view),
    path('about', HomeView.as_view())
]
