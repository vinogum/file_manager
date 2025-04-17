from django.contrib.auth.models import User
from django.db import models
from .utilities import upload_to
import os
import shutil
from file_manager import settings
from django.core.exceptions import ValidationError
from django.db.models import F


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        unique_together = ("user", "url")

    def delete(self, *args, **kwargs):
        if not self.pk:
            raise ValidationError("File object must be saved before deletion.")

        user_folder = f"user_{self.user.id}"
        versions_directory = f"file_{self.id}"

        # Create media/user_id/file_id/ path
        file_versions_dir = os.path.join(
            settings.MEDIA_ROOT, user_folder, versions_directory
        )

        if os.path.isdir(file_versions_dir):
            shutil.rmtree(file_versions_dir)

        super().delete(*args, **kwargs)


class FileVersion(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name="versions")
    version = models.PositiveIntegerField()
    file_data = models.FileField(upload_to=upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("file", "version")

    def delete(self, *args, **kwargs):
        if not self.pk:
            raise ValidationError("FileVersion object must be saved before deletion.")

        # Get the queryset of versions with a greater version number
        version_gt = FileVersion.objects.filter(
            file=self.file, version__gt=self.version
        )

        super().delete(*args, **kwargs)

        if version_gt.exists():
            version_gt.update(version=F("version") - 1)

        file = self.file_data.path
        if not os.path.isfile(file):
            raise ValidationError(f"Such file does not exist: {file}")
        os.remove(file)

    def save(self, *args, **kwargs):
        last_version = (
            FileVersion.objects.filter(file=self.file).order_by("-version").first()
        )

        if last_version:
            self.version = last_version.version + 1
        else:
            self.version = 0

        super().save(*args, **kwargs)
