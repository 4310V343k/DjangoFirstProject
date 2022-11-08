from django.db import models


class Title(models.Model):
    russian_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100, default='')
    alternative_names = models.CharField(max_length=300, default='')
    description = models.TextField(default='')
    tags = models.ManyToManyField('api.Tag', related_name='titles_with_tag+', blank=True)

    class Meta:
        ordering = ['russian_name']
