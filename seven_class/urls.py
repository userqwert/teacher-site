from django.urls import path

from .views import (
    ObjectListView,
    ObjectDetailView,
)

urlpatterns = [
    path("", ObjectListView.as_view(), name="object_list"),
    path("<uuid:pk>", ObjectDetailView.as_view(), name="object_detail"),
]
