from app.models import Foobar
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse


class FoobarTestCase(TestCase):
    def setUp(self):
        upload = SimpleUploadedFile("foo.txt", b"abc", content_type="text/txt")
        self.obj = Foobar.objects.create(foo=upload)

    def test_create_model(self):
        # Then: file is stored in the safe vault
        self.assertTrue(self.obj.foo.path.startswith(settings.SAFE_MEDIA_ROOT))
        # Then: content can be read unencrypted
        with self.obj.foo.open() as f:
            self.assertEqual(f.read(), b"abc")
        # Then: plain content is encrypted
        with open(self.obj.foo.path, "rb") as f:
            self.assertNotEqual(f.read(), b"abc")

    def test_view_file_content(self):
        """Test the view that retrieves the encrypted file content"""
        client = Client()
        url = reverse("app:foobar_view", args=[self.obj.pk])
        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(b"abc", response.content)
