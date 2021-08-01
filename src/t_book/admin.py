from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-id',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    ordering = ('-id',)
    list_filter = ('author',)
    search_fields = ('name',)
