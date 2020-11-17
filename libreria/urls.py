from django.urls import path

from .views import AutoreDetail, LibroList, AutoreList
app_name = "libreria"
urlpatterns = [
    path('', LibroList.as_view(), name='lista_libri'),
    path('autore/<int:pk>/', AutoreDetail.as_view(), name='profilo_autore'),
    path('lista_autori/', AutoreList.as_view(), name='lista_autori'),
]
