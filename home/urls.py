from django.urls import path
from .views import home, about, contact


urlpatterns= [
    path('', home, name = 'homeview'),
    path('about-me/for-me/for-us/',about, name = 'aboutview'),
    path('contact-me/', contact, name = 'contactview')
]