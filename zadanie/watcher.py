import os
import time
import django
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zadanie.settings')
django.setup()

from main.models import UploadedFile

class Watcher:
    DIRECTORY_TO_WATCH = "C:/Users/aleks/Desktop/ZadanieRekrutacja/zadanie/uploads"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'deleted':
            print(f'File {event.src_path} was deleted')
            try:
                file_name = event.src_path.split('\\')[-1]
                print(file_name)
                UploadedFile.objects.filter(file__contains=file_name).delete()
            except Exception as e:
                print(str(e))

print("Observer started")
w = Watcher()
w.run()