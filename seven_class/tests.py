from django.test import TestCase
from django.urls import reverse
from .models import Object7


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.object = Object7.objects.create(
            name="Harry Potter",
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.object.name}", "Harry Potter")

    def test_book_list_view(self):
        response = self.client.get(reverse("object_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "education_classes/object_list.html")

    def test_book_detail_view(self):
        response = self.client.get(self.object.get_absolute_url())
        no_response = self.client.get("/7-klas/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "education_classes/object_detail.html")
