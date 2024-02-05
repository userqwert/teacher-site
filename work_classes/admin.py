from django.contrib import admin
from .models import WorkClass, Lesson


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1


class WorkClassAdmin(admin.ModelAdmin):
    inlines = [
        LessonInline,
    ]


admin.site.register(WorkClass, WorkClassAdmin)
