from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=4, primary_key=True)
    title = models.TextField()
    author = models.TextField()
    published_year = models.IntegerField()

class Student(models.Model):
    student_id = models.CharField(max_length=4, primary_key=True)
    student_name = models.CharField(max_length=15)
    student_phone = models.CharField(max_length=12)
    student_email = models.EmailField()
    stud_status = models.TextField(default='Active')    

class Borrowing(models.Model):
    borrow_id = models.CharField(max_length=4, primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()

class Course(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    description = models.TextField()

class Mentor(models.Model):
    menid = models.CharField(max_length=3, primary_key=True)
    menname = models.TextField(max_length=255)
    menroomno = models.CharField(max_length=3, default='sk2')