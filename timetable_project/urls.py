from django.contrib import admin
from django.urls import path
from timetable import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_add, name='department_add'),
    path('departments/edit/<int:pk>/', views.department_edit, name='department_edit'),
    path('departments/delete/<int:pk>/', views.department_delete, name='department_delete'),
    
    path('faculty/', views.faculty_list, name='faculty_list'),
    path('faculty/add/', views.faculty_add, name='faculty_add'),
    path('faculty/edit/<int:pk>/', views.faculty_edit, name='faculty_edit'),
    path('faculty/delete/<int:pk>/', views.faculty_delete, name='faculty_delete'),
    
    path('classrooms/', views.classroom_list, name='classroom_list'),
    path('classrooms/add/', views.classroom_add, name='classroom_add'),
    path('classrooms/edit/<int:pk>/', views.classroom_edit, name='classroom_edit'),
    path('classrooms/delete/<int:pk>/', views.classroom_delete, name='classroom_delete'),
    
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_add, name='course_add'),
    path('courses/edit/<int:pk>/', views.course_edit, name='course_edit'),
    path('courses/delete/<int:pk>/', views.course_delete, name='course_delete'),
    
    path('timeslots/', views.timeslot_list, name='timeslot_list'),
    path('timeslots/add/', views.timeslot_add, name='timeslot_add'),
    path('timeslots/edit/<int:pk>/', views.timeslot_edit, name='timeslot_edit'),
    path('timeslots/delete/<int:pk>/', views.timeslot_delete, name='timeslot_delete'),
    
    path('student-groups/', views.studentgroup_list, name='studentgroup_list'),
    path('student-groups/add/', views.studentgroup_add, name='studentgroup_add'),
    path('student-groups/edit/<int:pk>/', views.studentgroup_edit, name='studentgroup_edit'),
    path('student-groups/delete/<int:pk>/', views.studentgroup_delete, name='studentgroup_delete'),
    
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assignments/add/', views.assignment_add, name='assignment_add'),
    path('assignments/delete/<int:pk>/', views.assignment_delete, name='assignment_delete'),
    
    path('generate/', views.generate_timetable, name='generate_timetable'),
    path('timetable/', views.timetable_view, name='timetable_view'),
    path('timetable/faculty/', views.timetable_by_faculty, name='timetable_by_faculty'),
    path('timetable/classroom/', views.timetable_by_classroom, name='timetable_by_classroom'),
    path('timetable/group/', views.timetable_by_group, name='timetable_by_group'),
    path('timetable/delete/<int:pk>/', views.entry_delete, name='entry_delete'),
    path('timetable/clear/', views.entry_delete_all, name='entry_delete_all'),
    
    path('', views.dashboard, name='home'),
]
