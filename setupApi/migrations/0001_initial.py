# Generated by Django 5.0.6 on 2024-05-14 21:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=300, verbose_name='Descrição')),
                ('preco', models.FloatField(verbose_name='Preço')),
                ('estoque', models.SmallIntegerField(blank=True, verbose_name='Quantidade em Estoque')),
                ('codigo', models.BigIntegerField(verbose_name='Código de Barras')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setupApi.categoria')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.SmallIntegerField(verbose_name='Quantidade')),
                ('data_entrada', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setupApi.produto')),
            ],
            options={
                'verbose_name': 'Data de Entrada',
            },
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.SmallIntegerField(verbose_name='Quantidade')),
                ('data_saida', models.DateTimeField(auto_now_add=True, verbose_name='Data de Saída')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setupApi.produto')),
            ],
        ),
    ]