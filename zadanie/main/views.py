from django.shortcuts import redirect, render
from .forms import FileUploadForm
from django.contrib import messages

def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=True)
            messages.success(request, 'File uploaded successfully!')
            return redirect('file_upload')
        else: 
            messages.error(request, 'There was an error when uploading the file')
    else:
        form = FileUploadForm()
    return render(request, 'main/upload.html', {'form': form})