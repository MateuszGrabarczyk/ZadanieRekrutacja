from django.contrib import admin
from .models import UploadedFile

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'uploaded_at')
    list_filter = ('uploaded_at',)

    def filename(self, obj):
        return obj.file.name.split('/')[-1]

admin.site.register(UploadedFile, UploadedFileAdmin)
