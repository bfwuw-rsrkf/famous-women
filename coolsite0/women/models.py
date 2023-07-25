from django.db import models


class Woman(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to="Images")
    time_created = models.DateField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()

    def __str__(self):
        return self.title
