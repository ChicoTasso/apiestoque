from django.urls import path
from .views import CategoriaListCreate, CategoriaRetrieveDestroy, ProdutoListCreate, ProdutoRetrieveDestroy, EntradaListCreate, EntradaRetrieveDestroy, SaidaListCreate, SaidaRetrieveDestroy, home
urlpatterns = [
    path('', home, name='home'),
    path('categorias/', CategoriaListCreate.as_view(), name='categorias-list-create'),
    path('produtos/', ProdutoListCreate.as_view(), name='produtos-list-create'),
    path('entradas/', EntradaListCreate.as_view(), name='entrada-list-create'),
    path('saidas/', SaidaListCreate.as_view(), name='saida-list-create'),
    path('categorias/<int:pk>/', CategoriaRetrieveDestroy.as_view(), name='categoria-retrieve-destroy'),
    path('produtos/<int:pk>', ProdutoRetrieveDestroy.as_view(), name='produto-retrieve-destroy'),
    path('entradas/<int:pk>/', EntradaRetrieveDestroy.as_view(), name='entrada-retrieve-destroy'),
    path('saidas/<int:pk>/', SaidaRetrieveDestroy.as_view(), name='saida-retrieve-destroy'),
]