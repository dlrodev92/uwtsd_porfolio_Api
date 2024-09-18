from django.db import models
from technology.models import Technology
from tag.models import Tag
from file.models import File
from image.models import Image

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    repo = models.URLField(max_length=500)  
    technologies = models.ManyToManyField(Technology, related_name='projects')  
    tags = models.ManyToManyField(Tag, related_name='projects')   
    files = models.ManyToManyField(File, related_name='projects', blank=True)  
    images = models.ManyToManyField(Image, related_name='projects', blank=True)  


    def __str__(self):
        return self.title

class Subtitle(models.Model):
    project = models.ForeignKey(Project, related_name='subtitles', on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.subtitle

class Paragraph(models.Model):
    project = models.ForeignKey(Project, related_name='paragraphs', on_delete=models.CASCADE)
    paragraph = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.paragraph

class Reference(models.Model):
    project = models.ForeignKey( Project, related_name='references', on_delete=models.CASCADE)
    reference = models.CharField(max_length=100)

    def __str__(self):
        return self.reference
    