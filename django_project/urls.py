from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path("boss/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local apps
    path("", include("pages.urls")),
    # namespace для возможности использовать один шаблон для нескольких УРЛ, его нужно внести в модель и шаблон
    path("music/", include(("music.urls", "music"), namespace="music")),
    path(
        "work-classes/",
        include(("work_classes.urls", "work_classes"), namespace="work"),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
