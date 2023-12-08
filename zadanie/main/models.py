import os
from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name.split('/')[-1]

    def delete(self, *args, **kwargs):
        # Full path to the file
        file_path = self.file.path

        # Delete the model before the file
        super(UploadedFile, self).delete(*args, **kwargs)

        # Now delete the file if it exists
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
            except OSError as e:  # This handles things like the file being open/used elsewhere
                # Log the error or send a notification (recommended)
                print(f'Error deleting file {file_path}: {e.strerror}')