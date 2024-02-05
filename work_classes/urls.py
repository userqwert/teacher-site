from django.urls import path

from .views import (
    ObjectListView,
    ObjectDetailView,
    LessonDetailView,
)

app_name = "work_classes"

urlpatterns = [
    path("", ObjectListView.as_view(), name="class_list"),
    path("<uuid:pk>", ObjectDetailView.as_view(), name="lessons_list"),
    path("<uuid:pk>/lesson-detail", LessonDetailView.as_view(), name="lesson_detail"),
]
