from django.views.generic import ListView, DetailView

from .models import Object7, Lesson


class ObjectListView(ListView):
    model = Object7
    template_name = "education_classes/object_list.html"


class ObjectDetailView(DetailView):
    model = Object7
    context_object_name = "subject"
    template_name = "education_classes/object_detail.html"


class LessonDetailView(DetailView):
    model = Lesson
    context_object_name = "lesson"
    template_name = "education_classes/lesson_detail.html"
