from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
from django.contrib import messages
# Create your views here.

def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image uploaded successfully")
            return redirect('view_images')
        else :
            messages.error(request, "Image upload failed")
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def view_images(request):
    images = Image.objects.all()
    return render(request, 'view_images.html', {'images': images})
 