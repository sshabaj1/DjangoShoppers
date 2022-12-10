from django.db import models
from django.core.validators import FileExtensionValidator



class AboutComponent(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='about/video',null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    image = models.ImageField(upload_to='about/photo',
                              blank=True)
    available = models.BooleanField(default=True)