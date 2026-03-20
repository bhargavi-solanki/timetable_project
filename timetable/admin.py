from django.contrib import admin
from .models import Department, Faculty, Classroom, Course, TimeSlot, StudentGroup, CourseAssignment, TimetableEntry

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name', 'code']

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'department', 'phone']
    list_filter = ['department']
    search_fields = ['name', 'email']

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['name', 'building', 'capacity', 'room_type']
    list_filter = ['building', 'room_type']
    search_fields = ['name', 'building']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'credit_hours', 'department', 'assigned_faculty']
    list_filter = ['department']
    search_fields = ['name', 'code']

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'is_break']
    list_filter = ['day', 'is_break']
    ordering = ['day', 'start_time']

@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'year', 'semester']
    list_filter = ['department', 'year', 'semester']
    search_fields = ['name']

@admin.register(CourseAssignment)
class CourseAssignmentAdmin(admin.ModelAdmin):
    list_display = ['course', 'student_group', 'faculty']
    list_filter = ['student_group']
    search_fields = ['course__name', 'student_group__name']

@admin.register(TimetableEntry)
class TimetableEntryAdmin(admin.ModelAdmin):
    list_display = ['course_assignment', 'classroom', 'time_slot']
    list_filter = ['time_slot__day']
    search_fields = ['course_assignment__course__name']
