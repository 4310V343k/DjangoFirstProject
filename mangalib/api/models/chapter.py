from django.db import models


class Chapter(models.Model):
    volume = models.ForeignKey('api.Volume', related_name='chapters', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.IntegerField()

    watch_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['volume', 'position']

    def __str__(self):
        return '%s: %s' % (self.position, self.name)