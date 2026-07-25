from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import task

# Create your views here.

def task_list(request):
    tasks = task.objects.all().order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title:
            task.objects.create(title=title, description=description)
            return redirect('form')
        else:
            return HttpResponse('Please provide a title for the task.')

    return render(request, 'add_task.html')

def update_task(request, task_id):
    task_instance = get_object_or_404(task, id=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'

        if title:
            task_instance.title = title
            task_instance.description = description
            task_instance.completed = completed
            task_instance.save()
            return redirect('form')
        else:
            return HttpResponse('Please provide a title for the task.')

    return render(request, 'update_task.html', {'task': task_instance})



def delete_task(request, task_id):
    task_instance = get_object_or_404(task, id=task_id)
    if not task_instance.completed:
        return HttpResponse('Cannot delete an incomplete task. Please mark it as completed first.')
    task_instance.delete()
    return redirect('form')


def edit_task(request, task_id):    
    task_instance = get_object_or_404(task, id=task_id)
    return render(request, 'edit_task.html', {'task': task_instance})


def toggle_task(request, task_id):
    task_instance = get_object_or_404(task, id=task_id)
    task_instance.completed = not task_instance.completed
    task_instance.save()
    return redirect('form')