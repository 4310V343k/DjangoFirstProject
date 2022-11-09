from django.db import models


class Volume(models.Model):
    title = models.ForeignKey('api.Title', related_name='volumes', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cost = models.IntegerField(default=0)
    position = models.IntegerField()

    class Meta:
        ordering = ['title', 'position']

    def __str__(self):
        return '%s: %s' % (self.position, self.name)
