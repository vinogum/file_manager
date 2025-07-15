from django.core.files import uploadedfile
from django.core import files
import hashlib
import os


def upload_to(instance, filename):
    if not hasattr(instance, "file_data"):
        raise ValueError("The instance has not attribute as 'file_data'!")

    file_hash = get_file_hash(instance.file_data)

    if file_hash is None:
        raise ValueError("Failed to get the hash of the file!")

    ext = filename.split(".")[-1]
    new_filename = f"{file_hash}.{ext}"
    basedir = f"user_{instance.file.user.id}/file_{instance.file.id}/"

    return os.path.join(basedir, new_filename)


def get_file_hash(file):
    if isinstance(file, uploadedfile.InMemoryUploadedFile):
        binary_data = file.read()
        hash_object = hashlib.sha256(binary_data)
        return hash_object.hexdigest()

    elif isinstance(file, files.File):
        binary_data = file.read()
        hash_object = hashlib.sha256(binary_data)
        return hash_object.hexdigest()

    elif isinstance(file, str) and os.path.isfile(file):
        with open(file, "rb") as filestream:
            binary_data = filestream.read()
            hash_object = hashlib.sha256(binary_data)
            return hash_object.hexdigest()
    else:
        return None
