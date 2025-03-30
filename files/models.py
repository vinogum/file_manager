from django.contrib.auth.models import User
from django.db import models
from .utilities import upload_to


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
