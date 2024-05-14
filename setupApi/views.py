from rest_framework import generics
from .models import Categoria, Produto, Entrada, Saida
from .serializer import CategoriaSerializer, ProdutoSerializer, EntradaSerializer, SaidaSerializer
from django.shortcuts import render



class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
class CategoriaRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer



class ProdutoListCreate(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
class ProdutoRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer



class EntradaListCreate(generics.ListCreateAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
class EntradaRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer



class SaidaListCreate(generics.ListCreateAPIView):
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer
class SaidaRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Saida.objects.all()
    serializer_class = SaidaSerializer

def home(request):
    template_name = 'home.html'
    context = {

    }
    return render(request, template_name, context)

