from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)
    imageUrl = models.URLField(max_length=500)

    def __str__(self):
        return self.name
    