from app.models import Foobar

from encrypted_files.views import EncryptedFileDetailView


class FoobarView(EncryptedFileDetailView):
    """View example.

    model: The model class
    encrypted_file_field: the field that contains the encrypted file.
    """

    model = Foobar
    encrypted_file_field = "foo"
