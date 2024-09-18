from django.db import models

class File(models.Model):
    name = models.CharField(max_length=100)
    fileUrl = models.URLField(max_length=500)

    def __str__(self):
        return self.name
    