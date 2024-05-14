from django.urls import path, include
from .views import CategoriaListCreate, CategoriaRetrieveDestroy, ProdutoListCreate, ProdutoRetrieveDestroy, EntradaListCreate, EntradaRetrieveDestroy, SaidaListCreate, SaidaRetrieveDestroy
urlpatterns = [
    path('categorias/', CategoriaListCreate.as_view(), name='categorias-list-create'),
    path('produtos/', ProdutoListCreate.as_view(), name='produtos-list-create'),
    path('entradas/', EntradaListCreate.as_view(), name='entrada-list-create'),
    path('saidas/', SaidaListCreate.as_view(), name='saida-list-create'),
    path('categorias/<int:pk>/',)
]