from django.db import models


# Create your models here.


class Welcome(models.Model):
    TopMessage = models.CharField(max_length=50)
    paragraph = models.CharField(max_length=100)

    def __str__(self):
        return self.TopMessage

class Students(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/', default='profile.png')


    def __str__(self):
        return self.name


class Courses(models.Model):
    name=models.CharField(max_length=200,null=True)
    duration=models.IntegerField(default=3,null=True,blank=True)
    fees=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.name)


# class Courses(models.Model):
#     name=models.CharField(max_length=200,null=True)
#     duration=models.IntegerField(default=3,null=True,blank=True)
#     fees=models.IntegerField(null=True,blank=True)
#     description=models.CharField(null=True,blank=True,max_length=10000)
#     def __str__(self):
#         return str(self.name)

# class Teacher(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)
#     description = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='images')
#
#     def __str__(self):
#         return str(self.name)
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    # Name2 = models.CharField(max_length=50)
    # description2 = models.CharField(max_length=100)
    # Name3 = models.CharField(max_length=50)
    # description3 = models.CharField(max_length=100)

    def __str__(self):
        return self.name

