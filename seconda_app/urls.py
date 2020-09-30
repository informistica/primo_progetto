from django.urls import path
from .views import esempio_if,esempio_ifelse
app_name = 'seconda_app'
urlpatterns = [
    path('if', esempio_if, name='if'),
    path('ifelse', esempio_ifelse, name='ifelse'),
]