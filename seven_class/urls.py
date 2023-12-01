from django.urls import path

from .views import (
    ObjectListView,
    ObjectDetailView,
    LessonDetailView,
)

urlpatterns = [
    path("", ObjectListView.as_view(), name="object_list"),
    path("<uuid:pk>", ObjectDetailView.as_view(), name="object_detail"),
    path("<uuid:pk>/lesson-detail", LessonDetailView.as_view(), name="lesson_detail"),
]
