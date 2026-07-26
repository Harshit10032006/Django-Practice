from django.shortcuts import render
from .form import StudentForm
from .models import Student
from django.shortcuts import get_object_or_404
# Create your views here.


def student_create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'app1/success.html')
        return render(request, 'app1/student_form.html', {'form': form})
    return render(request, 'app1/student_form.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'app1/student_list.html', {'students': students})


def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'app1/success.html')
        return render(request, 'app1/student_form.html', {'form': form})
    return render(request, 'app1/student_form.html', {'form': form})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return render(request, 'app1/success.html')