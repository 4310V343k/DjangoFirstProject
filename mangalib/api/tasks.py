import time

from mangalib.api.models import Chapter
from mangalib.celery import app
from django.db import transaction


@app.task
def increment_chapter_watch(pk):
    with transaction.atomic():
        inst = Chapter.objects.get(pk=pk)
        inst.watch_count += 1
        inst.save()


@app.task
def increment_chapter_like(pk):
    with transaction.atomic():
        inst = Chapter.objects.get(pk=pk)
        inst.like_count += 1
        inst.save()
