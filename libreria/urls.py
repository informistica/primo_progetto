from django.urls import path

from .views import AutoreDetail, LibroList

urlpatterns = [
    path('', LibroList.as_view(), name='lista_libri'),
    path('autore/<int:pk>/', AutoreDetail.as_view(), name='profilo_autore')
]
