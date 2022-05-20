from django.urls import path
from .views import home, about, contact


urlpatterns= [
    path('', home),
    path('about-me/for-me/for-us/',about),
    path('contact-me/', contact)
]