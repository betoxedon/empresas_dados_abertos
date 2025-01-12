# Generated by Django 5.0.3 on 2024-03-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14)),
                ('natju', models.CharField(max_length=255)),
                ('razao_social', models.CharField(max_length=255)),
                ('nome_fantasia', models.CharField(max_length=255)),
                ('cnae_descricao', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
    ]
