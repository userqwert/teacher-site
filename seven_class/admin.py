from django.contrib import admin
from .models import Object7, Lesson


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1


class Object7Admin(admin.ModelAdmin):
    inlines = [
        LessonInline,
    ]


admin.site.register(Object7, Object7Admin)
