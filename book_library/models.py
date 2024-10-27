from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100 , null=False  , blank=False)
    author = models.CharField(max_length=100 , null=False , blank=False)
    published_date = models.DateField(null=True)
    isbn = models.CharField(max_length=100 , null=False , blank=False , unique=True)
    pages = models.IntegerField(null=False , blank=False)
    cover = models.URLField(null=True)
    language = models.CharField(max_length=100 , null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} by {self.author}"

