from django.shortcuts import render, redirect
from .models import Student


# CREATE
def add_student(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        Student.objects.create(
            name=name,
            email=email,
            age=age
        )

        return redirect('student_list')

    return render(request, 'add_student.html')


# READ
def student_list(request):

    students = Student.objects.all()

    return render(request, 'student_list.html', {
        'students': students
    })


# UPDATE
def update_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":

        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')

        student.save()

        return redirect('student_list')

    return render(request, 'update_student.html', {
        'student': student
    })


# DELETE
def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect('student_list')