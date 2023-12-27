from django.db import models

from encrypted_files.fields import EncryptedFileField


class Foobar(models.Model):
    foo = EncryptedFileField(upload_to="somewhere/")
