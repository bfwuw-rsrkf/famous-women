from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Woman(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL", null=True)
    photo = models.ImageField(upload_to="Images", blank=True, null=True)
    time_created = models.DateField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
