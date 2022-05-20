from subprocess import check_output
from django.urls import path
from .views import signup, login, checkout

urlpatterns= [
path('signup/', signup),
path('login/', login),
path('checkout/', checkout),

]