from django.db import models




class Categoria(models.Model):

    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)

    def __str__(self):
        return f'{self.nome}'


    class Meta:

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Produto(models.Model):

    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=300)
    preco = models.FloatField('Preço')
    estoque = models.SmallIntegerField('Quantidade em Estoque', blank=True)
    codigo = models.BigIntegerField('Código de Barras', max_length=10)
    categoria = models.ForeignKey(Categoria,'Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.codigo}'


    class Meta:

        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'



class Entrada(models.Model):

    produto = models.ForeignKey(Produto, 'Produto')
    quantidade = models.SmallIntegerField('Quantidade', )
    data_entrada = models.DateTimeField('Data de Entrada', auto_now_add=True)

    def __str__(self):
        return f'{self.produto} - {self.data_entrada} - {self.quantidade}'


    class Meta:

        verbose_name = 'Data de Entrada'

class Saida(models.Model):

    
    produto = models.ForeignKey(Produto, 'Produto')
    quantidade = models.SmallIntegerField('Quantidade', )
    data_saida = models.DateTimeField('Data de Saída', auto_now_add=True)

    def __str__(self):
        return f'{self.produto} - {self.data_saida} - {self.quantidade}'

    
        

    
    
