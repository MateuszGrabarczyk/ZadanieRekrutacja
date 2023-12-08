To properly run Django app, make sure you have Django installed.
If not, run pip install django.

To run the app, run this command:
python manage.py runserver

This app lets user upload the file to the system. The user gets information wheather it was successful or not.
The file is stored in the database (object, but the file is physically on the computer in folder \uploads).

I added the watcher.py that you can run using this command:
python watcher.py

This script is the observer for the folder \uploads. 
If the file is manually deleted from the folder, the object is deleted as well.
