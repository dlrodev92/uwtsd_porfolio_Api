from rest_framework import serializers
from .models import Project, Subtitle, Paragraph, Reference

class SubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtitle
        fields = ['id', 'subtitle', 'order', 'project']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'paragraph', 'order', 'project']

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id', 'reference', 'project']

class ProjectSerializer(serializers.ModelSerializer):
    subtitles = SubtitleSerializer(many=True, read_only=True)
    paragraphs = ParagraphSerializer(many=True, read_only=True)
    references = ReferenceSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'date', 'repo', 'technologies', 'tags', 'files', 'images', 'subtitles', 'paragraphs', 'references']
