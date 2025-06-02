from django.db import models


class hr(models.Model):
    # User model fields
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
