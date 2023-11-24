from django.views.generic import ListView, DetailView

from .models import Object7


class ObjectListView(ListView):
    model = Object7
    template_name = "education_classes/object_list.html"


class ObjectDetailView(DetailView):
    model = Object7
    context_object_name = "subject"
    template_name = "education_classes/object_detail.html"
