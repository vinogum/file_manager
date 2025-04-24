from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from file_manager import settings
from .models import File, FileVersion
from django.core.files.base import File as DjangoFile
import shutil
import os
import io


class BaseTestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        # Check if user is authenticated
        self.client.login(username="testuser", password="testpassword")

        # Create a test django file
        file_path = os.path.join(settings.MEDIA_ROOT, "server", "images.jfif")
        self.assertTrue(os.path.isfile(file_path))
        with open(file_path, "rb") as f:
            bytes = f.read()
            file_obj = io.BytesIO(bytes)
            self.file = DjangoFile(file_obj, name="testfile")

        # Create a test file object
        self.file_model = File.objects.create(user=self.user, url="testpath/test.jpg")

    def tearDown(self):
        # Clean up any created files or directories
        userdir = os.path.join(settings.MEDIA_ROOT, "user_" + str(self.user.id))
        if os.path.isdir(userdir):
            shutil.rmtree(userdir)


class FileViewSetTest(BaseTestCase):
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


class FileVersionViewSetTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.version = FileVersion.objects.create(
            file=self.file_model, file_data=self.file
        )

    def test_list(self):
        url = reverse("file-versions-list", args=[self.file_model.id])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        url = reverse(
            "file-versions-detail", args=[self.file_model.id, self.version.id]
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
