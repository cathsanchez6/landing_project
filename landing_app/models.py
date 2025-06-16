# landing_app/models.py

from django.db import models

class LandingData(models.Model):
    BACKGROUND_CHOICES = [
        ('blue', 'Azul'),
        ('green', 'Verde'),
        ('white', 'Blanco'),
        ('black', 'Negro'),
    ]

    background = models.CharField(max_length=20, choices=BACKGROUND_CHOICES)
    logo = models.ImageField(upload_to='logos/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
