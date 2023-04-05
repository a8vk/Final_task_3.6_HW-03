from django.db import models
from django.shortcuts import reverse


class New(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    data_pub = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128, unique=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)
