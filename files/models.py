from django.core.files import uploadedfile
from django.core import files
from django.db import models
from django.contrib.auth.models import User
import hashlib
import os


def get_file_hash(file):
    if isinstance(file, uploadedfile.InMemoryUploadedFile):
        binary_data = file.read() # Get binary content of the file
        hash_object = hashlib.sha256(binary_data) # Get the hash of binary content as hash_object
        return hash_object.hexdigest() # Convert the hash_object to readable format (string)
    
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


def upload_to(instance, filename):
    if not hasattr(instance, "file_data"):
        raise ValueError("The instance has not attribute as 'file_data'!")
    
    file_hash = get_file_hash(instance.file_data)

    if file_hash == None:
        raise ValueError("Failed to get the hash of the file!")

    ext = filename.split('.')[-1]
    new_filename = f"{file_hash}.{ext}"
    basedir = f"user_{instance.file.id}/file_{instance.file.id}/"

    return os.path.join(basedir, new_filename)


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        unique_together = ("user", "url")


class FileVersion(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    version = models.PositiveIntegerField()
    file_data = models.FileField(upload_to=upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("file", "version")

    def save(self, *args, **kwargs):
        last_version = FileVersion.objects.filter(file=self.file).order_by("-version").first()

        if last_version:
            self.version = last_version.version + 1
        else:
            self.version = 0

        super().save(*args, **kwargs)
