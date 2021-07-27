from django.contrib import admin
from .models import Livro


class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'subtitulo', 'idioma',
                    'autor', 'editora', 'disponivel', 'emprestado')
    list_filter = ('autor', 'editora', 'idioma')
    list_display_links = ('id', 'titulo')
    list_per_page = 15
    search_fields = ('titulo', 'subtitulo', 'autor', 'editora')
    list_editable = ('disponivel','emprestado')


admin.site.register(Livro, LivroAdmin)
