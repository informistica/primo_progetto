from django.urls import path
from .views import homepage, menu

urlpatterns = [
    path('welcome/', homepage, name='home'),
    path('menu/', menu, name='menu'),

]



