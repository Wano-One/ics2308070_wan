from django.contrib import admin
from .models import Book, Student, Borrowing, Course, Mentor

# Register your models here.
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrowing)
admin.site.register(Course)
admin.site.register(Mentor)