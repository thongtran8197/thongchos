from django.db import models
from django.db.models import FileField


class Book(models.Model):
    name = models.CharField(default="", max_length=255)
    file_upload = FileField(upload_to="upload/")
