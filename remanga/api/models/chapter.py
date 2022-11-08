from django.db import models


class Chapter(models.Model):
    volume = models.ForeignKey('api.Volume', related_name='volumes', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    cost = models.IntegerField()
    position = models.IntegerField()

    watch_count = models.IntegerField()
    like_count = models.IntegerField()

    class Meta:
        ordering = ['volume', 'position']
