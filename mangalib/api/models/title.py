from django.db import models


class Title(models.Model):
    russian_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100, default='', blank=True)
    alternative_names = models.CharField(max_length=300, default='', blank=True)
    description = models.TextField(default='', blank=True)
    tags = models.ManyToManyField('api.Tag', related_name='titles_with_tag+', blank=True)

    class Meta:
        ordering = ['russian_name']

    def __str__(self):
        return '%s' % self.russian_name
