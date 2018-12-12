from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    id = models.AutoField(
        primary_key=True,
        help_text='Unique ID of news entry',
    )
    title = models.CharField(
        max_length=100,
        help_text='News title',
    )
    contents = models.CharField(
        max_length=500,
        help_text='News message'
    )

    def __str__(self):
        return self.contents
