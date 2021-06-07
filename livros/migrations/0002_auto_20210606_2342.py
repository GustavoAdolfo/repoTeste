# Generated by Django 3.2.3 on 2021-06-06 23:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='data_cadastro',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='livro',
            name='capa',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='livro',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]