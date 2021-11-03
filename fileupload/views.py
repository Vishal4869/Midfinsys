from django.shortcuts import render, HttpResponse
from .models import FilesUpload
from django.contrib import messages
from datetime import datetime

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        file = request.FILES["file"]
        #document = FilesUpload.objects.create(file=file2)
        resumeupload = FilesUpload(name=name, file=file, date=datetime.today())
        resumeupload.save()
        messages.success(request, 'Thank you for Submitting your Resume,We will contact you shortly !')
    return render(request, "index.html")
