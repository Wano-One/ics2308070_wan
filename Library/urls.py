from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("view/",views.view, name='view'),
    path("dbstudent/",views.dbstudent, name='dbstudent'),
    path("dbbook/",views.dbbook, name='dbbook'),
    path("dbborrow/",views.dbbborrow, name='dbborrow'),
    path("course/",views.course, name='course'),
    path("mentor/",views.mentor, name='mentor'),
    path("course/update_course/<str:code>", views.update_course, name='update_course'),
    path("course/update_course/save_update_course/<str:code>", views.save_update_course, name='save_update_course'),
    path("course/delete_course/<str:code>", views.delete_course, name='delete_course'),
    path("mentor/update_mentor/<str:menname>", views.update_mentor, name='update_mentor'),
    path("mentor/update_mentor/save_update_mentor/<str:menname>", views.save_update_mentor, name='save_update_mentor'),
    path("mentor/delete_mentor/<str:menid>", views.delete_mentor, name='delete_mentor')
]