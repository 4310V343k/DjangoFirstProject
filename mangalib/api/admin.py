from django.contrib import admin

from mangalib.api.models import Title, Volume, Chapter


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    exclude = ['watch_count', 'like_count']
    pass


class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 0
    show_change_link = True


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):

    inlines = [ChapterInline]


class VolumeInline(admin.StackedInline):
    model = Volume
    extra = 0
    show_change_link = True


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    search_fields = [
        'russian_name', 'english_name',
        'alternative_names', 'description',
        'volumes__name', 'volumes__chapters__name'
    ]
    inlines = [VolumeInline]

