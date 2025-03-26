from django.db import models


class Document(models.Model):
    """Model to store collaborative documents"""

    name = models.CharField(max_length=255, unique=True)
    content = models.TextField(default="")  # models.BinaryField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
