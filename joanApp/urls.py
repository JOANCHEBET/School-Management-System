from django.urls import path

from . import views


app_name = 'joanApp'

urlpatterns = [
    path('', views.home, name='index.html'),
    path('course/', views.course, name='course.html'),
    path('teachers/', views.teachers, name='teachers.html'),
    path('programs/', views.programs, name='programs.html'),
    path('contacts/', views.contacts, name='contacts.html'),
    path('admission/', views.admission, name='admission.html'),
    path('students/', views.students, name='students.html'),
    path('viewdata', views.viewdata, name='viewdata.html'),
    path('delete/<id>', views.delete, name="delete"),
    path('insertdata', views.insertdata, name="insertdata"),
    path('edit/<id>', views.edit, name="edit"),
    path('details/<id>', views.details, name="details"),



]