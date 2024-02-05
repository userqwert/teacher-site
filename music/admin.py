from django.contrib import admin
from .models import MusicClass, Lesson


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1


class MusicClassAdmin(admin.ModelAdmin):
    inlines = [
        LessonInline,
    ]


admin.site.register(MusicClass, MusicClassAdmin)
