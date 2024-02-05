from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MusicClass, Lesson


class ObjectListView(LoginRequiredMixin, ListView):
    model = MusicClass
    template_name = "education_classes/class_list.html"


class ObjectDetailView(LoginRequiredMixin, DetailView):
    model = MusicClass
    context_object_name = "subject"
    template_name = "education_classes/lessons_list.html"


class LessonDetailView(LoginRequiredMixin, DetailView):
    model = Lesson
    context_object_name = "lesson"
    template_name = "education_classes/lesson_detail.html"
