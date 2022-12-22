from django.contrib import admin
from primeiro_app.models import Autor, Livro, Categoria, Usuario, Endereco


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    ...


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    ...


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    ...


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    ...

# Register your models here.
