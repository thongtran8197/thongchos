__author__ = "thong.tran@paradox.ai"
__date__ = "23/07/2021"

from rest_framework import serializers

from src.t_book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'name',
            'file_upload',
        ]
