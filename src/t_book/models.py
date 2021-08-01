from django.db import models
from django.db.models import FileField


class Author(models.Model):
    name = models.CharField(default="", max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(default="", max_length=255)
    file_upload = FileField(upload_to="upload/")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author", null=True)
