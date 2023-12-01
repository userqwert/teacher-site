from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase, Client
from django.urls import reverse
from .models import Object7, Lesson


class ClassTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создание пользователя
        cls.user = get_user_model().objects.create_user(
            username="reviewuser", email="reviewuser@email.com", password="testpass123"
        )

        # Создание предмета
        cls.object = Object7.objects.create(
            name="Harry Potter",
        )

        # Создание урока
        cls.lesson = Lesson.objects.create(
            subject=cls.object,
            title="Physics",
            content="текст для читача",
        )

    def test_class_listing(self):
        self.assertEqual(f"{self.object.name}", "Harry Potter")

    def test_class_list_view(self):
        response = self.client.get(reverse("object_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "education_classes/object_list.html")

    def test_class_detail_view_with_permissions(self):
        self.client.login(email="reviewuser@email.com", password="testpass123")
        response = self.client.get(self.object.get_absolute_url())
        no_response = self.client.get("/7-klas/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "education_classes/object_detail.html")

    def test_lesson_exists(self):
        lesson_exists = Lesson.objects.filter(title="Physics").exists()
        self.assertTrue(lesson_exists)

    def test_object_list_view_template(self):
        response = self.client.get(reverse("object_list"))
        self.assertTemplateUsed(response, "education_classes/object_list.html")

    def test_lesson_detail_view_content(self):
        response = self.client.get(self.lesson.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "текст для читача")
        self.assertContains(response, "Physics")
        self.assertTemplateUsed(response, "education_classes/lesson_detail.html")
