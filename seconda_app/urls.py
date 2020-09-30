from django.urls import path
from .views import esempio_if
app_name = 'seconda_app'
urlpatterns = [
    path('if', esempio_if, name='if'),
]