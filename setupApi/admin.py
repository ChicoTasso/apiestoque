from django.contrib import admin
from .models import Categoria, Produto, Entrada, Saida

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao','preco', 'quantidade', 'categoria']
    list_filter = ['categoria']
    search_fields = ['nome', 'descricao']

class EntradaAdmin(admin.ModelAdmin):
    list_display = ['produto', 'quantidade', 'data_entrada']
    list_filter = ['produto__nome', 'data_entrada']
    search_fields = ['produto__nome']

class SaidaAdmin(admin.ModelAdmin):
    list_display = ['produto', 'quantidade', 'data_saida']
    list_filter = ['produto__nome', 'data_saida']
    search_fields = ['produto__nome']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Saida, SaidaAdmin)
