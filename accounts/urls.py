from django.urls import path
from .views import signup, login, checkout

urlpatterns= [
path('', signup),
path('login/', login),
path('checkout/', checkout),

]