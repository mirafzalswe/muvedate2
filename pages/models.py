from django.db import models


from mdeditor.fields import MDTextField
from django.db import models

class Page(models.Model):
    TYPE_CHOICES = (
        ('tutorial', 'Tutorial'),
        ('video', 'Video'),
    )
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    # content = models.CharField(max_length=254)
    # video = models.URLField()
    def __str__(self):
        return self.title






class Tutorial(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='tutorials', null=True)
    content = MDTextField()

class Video(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='videos', null=True)
    video = models.URLField()


