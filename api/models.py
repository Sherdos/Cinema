from django.db import models

# Create your models here.
class Movie(models.Model):
    """Model definition for Movie."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/image')
    video = models.FileField(upload_to='movies/video')
    

    class Meta:
        """Meta definition for Movie."""

        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        """Unicode representation of Movie."""
        return f'{self.title}'
