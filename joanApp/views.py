
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Students, Welcome, Teacher, Course
from django.contrib import messages

import os


# Create your views here.

# here is where all functions are created


def home(request):
    school = Welcome.objects.all()[:1]

    context = {'school': school}

    return render(request, 'index.html', context)


def course(request):
    course = Course.objects.all()
    context = {'course': course}
    return render(request, 'course.html',  context)


# def teachers(request ):
#
#     return render(request, 'teachers.html')

def teachers(request):
    teacher= Teacher.objects.all()

    context = {'teacher': teacher}

    return render(request, 'teachers.html', context)

def programs(request):
    return render(request, 'programs.html')


def contacts(request):
    return render(request, 'contacts.html')

def admission(request):
    return render(request, 'admission.html', {'navbar': 'admission'})


def viewdata(request):
    students = Students.objects.all()
    return render(request, 'viewdata.html', {'students': students})


def delete(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    messages.success(request, 'Deleted successfully')
    return redirect("/viewdata")


def insertdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        image = request.FILES['image']

        room = Students(name=name, email=email, age=age, image=image)
        room.save()
        messages.success(request,  ' student added successfully')
        return redirect("/admission")


    return redirect("/admission")


def edit(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST['age']
        image = request.FILES['image']

        student = Students.objects.get(id=id)

        student.name = name
        student.email = email
        student.age = age
        student.image = image

        if len(request.FILES) != 0:
            if len(student.image) > 0:
                student.image = request.FILES['image']

        student.save()
        return redirect("/viewdata")

    student = Students.objects.get(id=id)
    return render(request, 'edit.html', {'student':student})


def details(request, id):
    student = Students.objects.get(id=id)
    return render(request, 'details.html', {'student':student})


def students(request):
    return redirect("/viewdata")