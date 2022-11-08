from django.db import models


class Volume(models.Model):
    title = models.ForeignKey('api.Title', related_name='volumes', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    cost = models.IntegerField()
    position = models.IntegerField()

    class Meta:
        ordering = ['position']
