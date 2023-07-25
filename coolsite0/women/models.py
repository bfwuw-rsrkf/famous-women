from django.db import models


class Woman(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="Images", blank=True, null=True)
    time_created = models.DateField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
