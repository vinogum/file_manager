from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
import requests
from file_manager import settings
from .models import File
import io
import os
import shutil


class FileViewSetTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        # Check if user is authenticated
        self.client.login(username="testuser", password="testpassword")

        # Create a test file
        response = requests.get(r"https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg")
        self.assertEqual(response.status_code, 200)
        self.file = io.BytesIO(response.content)
        self.file.name = "test.jpg"
        self.file_model = File.objects.create(user=self.user, url="testpath/test.jpg")

    def test_list(self):
        url = reverse("file-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        data = {
            "file_data": self.file,
            "url": "testpath/test.txt",
        }
        url = reverse("file-list")
        response = self.client.post(url, data, format="multipart")
        self.assertEqual(response.status_code, 201)

    def test_retrieve(self):
        url = reverse("file-detail", args=[self.file_model.id])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        url = reverse("file-detail", args=[self.file_model.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def tearDown(self):
        userdir = os.path.join(settings.MEDIA_ROOT, "user_" + {self.user.id})
        if os.path.isdir(userdir):
            shutil.rmtree(userdir)