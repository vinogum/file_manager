from django.contrib import admin
from .models import FileVersion, File

# Correct way to register models
admin.site.register(FileVersion)
admin.site.register(File)
