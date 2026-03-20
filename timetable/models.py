from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"{self.code} - {self.name}"
    
    class Meta:
        verbose_name_plural = "Departments"

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='faculty')
    available_days = models.JSONField(default=list)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Faculty"

class Classroom(models.Model):
    ROOM_TYPES = [
        ('lecture', 'Lecture Hall'),
        ('lab', 'Laboratory'),
        ('computer_lab', 'Computer Lab'),
    ]
    name = models.CharField(max_length=50)
    building = models.CharField(max_length=100)
    capacity = models.IntegerField()
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES, default='lecture')
    
    def __str__(self):
        return f"{self.name} ({self.building})"
    
    class Meta:
        verbose_name_plural = "Classrooms"

class Course(models.Model):
    COURSE_TYPES = [
        ('theory', 'Theory'),
        ('practical', 'Practical'),
    ]
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    credit_hours = models.IntegerField(default=3)
    course_type = models.CharField(max_length=20, choices=COURSE_TYPES, default='theory')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    assigned_faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_courses')
    
    def __str__(self):
        return f"{self.code} - {self.name}"
    
    class Meta:
        verbose_name_plural = "Courses"

class TimeSlot(models.Model):
    DAYS_OF_WEEK = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
    ]
    day = models.CharField(max_length=20, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_break = models.BooleanField(default=False)
    is_lunch = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.day.capitalize()} {self.start_time} - {self.end_time}"
    
    class Meta:
        verbose_name_plural = "Time Slots"
        ordering = ['day', 'start_time']

class StudentGroup(models.Model):
    SEMESTER_TYPES = [
        ('odd', 'Odd Semester'),
        ('even', 'Even Semester'),
    ]
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='student_groups')
    year = models.IntegerField()
    semester = models.IntegerField()
    semester_type = models.CharField(max_length=10, choices=SEMESTER_TYPES, default='odd')
    
    def __str__(self):
        sem_type = "Odd" if self.semester_type == 'odd' else "Even"
        return f"{self.name} - Year {self.year} Sem {self.semester} ({sem_type})"
    
    class Meta:
        verbose_name_plural = "Student Groups"

class CourseAssignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    student_group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE, related_name='course_assignments')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='teaching_assignments')
    
    class Meta:
        unique_together = ('course', 'student_group')
        verbose_name_plural = "Course Assignments"

class TimetableEntry(models.Model):
    course_assignment = models.ForeignKey(CourseAssignment, on_delete=models.CASCADE, related_name='timetable_entries')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='timetable_entries')
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='timetable_entries')
    
    def __str__(self):
        return f"{self.course_assignment} - {self.time_slot}"
    
    class Meta:
        verbose_name_plural = "Timetable Entries"
