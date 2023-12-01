from django.db import models
from django.urls import reverse
import uuid


class Object7(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Назва предмету")
    img_sub = models.ImageField(
        upload_to="covers/", blank=True, null=True, verbose_name="Картинка для предмету"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("object_detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Предмет"  # Изменяем имя модели
        verbose_name_plural = "Предмети"  # Изменяем имя модели во множественном числе


class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, verbose_name="Тема уроку")
    content = models.TextField(blank=True, null=True, verbose_name="Текс для читача")
    subject = models.ForeignKey(
        "Object7", on_delete=models.CASCADE, related_name="lessons"
    )
    # Добавляем поля для материалов урока
    images = models.ImageField(
        upload_to="covers/", blank=True, null=True, verbose_name="Картинка до уроку"
    )
    pdf_file = models.FileField(
        upload_to="lesson_files/", blank=True, null=True, verbose_name="ПДФ Файл"
    )
    presentation = models.FileField(
        upload_to="lesson_files/", blank=True, null=True, verbose_name="Презентація"
    )
    youtube_video_url = models.URLField(
        blank=True, null=True, verbose_name="Відео з YouTube"
    )
    docx_file = models.URLField(blank=True, null=True, verbose_name="DOCX Файл")
    google_form = models.URLField(
        blank=True, null=True, verbose_name="Форма для тестів"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("lesson_detail", args=[str(self.id)])
