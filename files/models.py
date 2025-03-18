from django.db import models
from django.contrib.auth.models import User

def upload_to(instance, filename):
    pass

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
