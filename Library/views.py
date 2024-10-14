from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Library.models import Student, Course, Mentor

# Create your views here.
def index(request):
    context = {
        'lastname':'Apan',
        'greeting':1,
    }
    return render(request, 'index.html',context)

def view(request):
    context = {
        'name':'Wan Arfan',
    }
    return render(request, 'view.html', context)

def dbstudent(request):
    mystudent = Student.objects.all().values()
    context = {
        'mystudent': mystudent,
    }
    return render(request, 'dbstudent.html', context)

def dbbook(request):
    return render(request, 'dbbook.html')

def dbbborrow(request):
    return render(request, 'dbborrow.html')

def course(request):
    cordb = Course.objects.all().values()
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data = Course(code=c_code, description=c_desc)
        data.save()
        dict = {
            'message':'Data Save'
        }
    else:
        dict = {
            'message':''
        }
    dict = {
        'cordata':cordb
    }

    return render(request, 'course.html', dict)

def mentor(request):
    mendb = Mentor.objects.all().values()
    if request.method == 'POST':
        mrid = request.POST['id']
        mrname = request.POST['name']
        mrroom = request.POST['room']
        data = Mentor(menid=mrid, menname=mrname, menroomno=mrroom)
        data.save()
        dict = {
            'message':'Data Save'
        }
    else:
        dict = {
            'message':''
        }
    dict = {
        'mendata':mendb
    }
        
    return render(request, 'newmentor.html', dict)

def update_course(request,code):
    data = Course.objects.get(code=code)
    dict = {
        'data':data
    }

    return render(request, 'update_course.html', dict)

def save_update_course(request,code):
    c_desc = request.POST['desc']
    data = Course.objects.get(code=code)
    data.description = c_desc
    data.save()

    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()

    return HttpResponseRedirect(reverse('course'))

def update_mentor(request,menname):
    data = Mentor.objects.get(menname=menname)
    dict = {
        'data':data
    }

    return render(request, 'update_mentor.html', dict)

def save_update_mentor(request,menname):
    c_mrroom = request.POST['room']
    data = Mentor.objects.get(menname=menname)
    data.menroomno = c_mrroom
    data.save()

    return HttpResponseRedirect(reverse("mentor"))

def delete_mentor(request,menid):
    data = Mentor.objects.get(menid=menid)
    data.delete()

    return HttpResponseRedirect(reverse('mentor'))
