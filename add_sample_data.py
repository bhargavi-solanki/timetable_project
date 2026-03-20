import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable_project.settings')
django.setup()

from timetable.models import Department, Faculty, Classroom, Course, TimeSlot, StudentGroup, CourseAssignment

print("Adding sample data...")

# Departments
dept1 = Department.objects.create(name="Computer Science & Engineering", code="CSE")
dept2 = Department.objects.create(name="Information Technology", code="IT")
dept3 = Department.objects.create(name="Electronics & Communication", code="ECE")
dept4 = Department.objects.create(name="Bachelor of Science", code="BSC")
print("Departments created")

# Faculty
fac1 = Faculty.objects.create(name="Dr. Ramesh Kumar", email="ramesh@cse.edu", phone="9876543210", department=dept1, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac2 = Faculty.objects.create(name="Dr. Priya Sharma", email="priya@cse.edu", phone="9876543211", department=dept1, available_days=["monday","tuesday","wednesday","thursday"])
fac3 = Faculty.objects.create(name="Dr. Amit Patel", email="amit@cse.edu", phone="9876543212", department=dept1, available_days=["tuesday","wednesday","thursday","friday"])
fac4 = Faculty.objects.create(name="Dr. Sneha Gupta", email="sneha@it.edu", phone="9876543213", department=dept2, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac5 = Faculty.objects.create(name="Dr. Vikram Singh", email="vikram@ece.edu", phone="9876543214", department=dept3, available_days=["monday","tuesday","wednesday","friday"])
print("Faculty created")

# Classrooms
Classroom.objects.create(name="Room 101", building="Block A", capacity=60, room_type="lecture")
Classroom.objects.create(name="Room 102", building="Block A", capacity=60, room_type="lecture")
Classroom.objects.create(name="Room 103", building="Block A", capacity=40, room_type="lecture")
Classroom.objects.create(name="Lab 301", building="Block B", capacity=30, room_type="lab")
Classroom.objects.create(name="Lab 302", building="Block B", capacity=30, room_type="lab")
Classroom.objects.create(name="Auditorium", building="Block C", capacity=200, room_type="lecture")
print("Classrooms created")

# Courses
course1 = Course.objects.create(name="Data Structures", code="CS201", credit_hours=4, department=dept1, assigned_faculty=fac1)
course2 = Course.objects.create(name="Database Management", code="CS301", credit_hours=3, department=dept1, assigned_faculty=fac2)
course3 = Course.objects.create(name="Operating Systems", code="CS302", credit_hours=3, department=dept1, assigned_faculty=fac3)
course4 = Course.objects.create(name="Python Programming", code="IT201", credit_hours=3, department=dept2, assigned_faculty=fac4)
course5 = Course.objects.create(name="Web Development", code="IT301", credit_hours=3, department=dept2, assigned_faculty=fac4)
course6 = Course.objects.create(name="Digital Electronics", code="EC201", credit_hours=4, department=dept3, assigned_faculty=fac5)
course7 = Course.objects.create(name="Computer Networks", code="CS401", credit_hours=3, department=dept1, assigned_faculty=fac1)
course8 = Course.objects.create(name="Machine Learning", code="CS402", credit_hours=3, department=dept1, assigned_faculty=fac2)
print("Courses created")

# Time Slots
days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
times = [
    ("09:00", "10:00"),
    ("10:00", "11:00"),
    ("11:00", "12:00"),
    ("12:00", "13:00"),
    ("13:00", "14:00"),
    ("14:00", "15:00"),
    ("15:00", "16:00"),
]
for day in days:
    for start, end in times:
        TimeSlot.objects.create(day=day, start_time=start, end_time=end, is_break=False)
print("Time slots created")

# Student Groups
group1 = StudentGroup.objects.create(name="CSE Year 1", department=dept1, year=1, semester=1)
group2 = StudentGroup.objects.create(name="CSE Year 2", department=dept1, year=2, semester=3)
group3 = StudentGroup.objects.create(name="CSE Year 3", department=dept1, year=3, semester=5)
group4 = StudentGroup.objects.create(name="CSE Year 4", department=dept1, year=4, semester=7)
group5 = StudentGroup.objects.create(name="IT Year 1", department=dept2, year=1, semester=1)
group6 = StudentGroup.objects.create(name="IT Year 2", department=dept2, year=2, semester=3)
group7 = StudentGroup.objects.create(name="ECE Year 1", department=dept3, year=1, semester=1)
print("Student groups created")

# Course Assignments
CourseAssignment.objects.create(course=course1, student_group=group1, faculty=fac1)
CourseAssignment.objects.create(course=course4, student_group=group1, faculty=fac4)
CourseAssignment.objects.create(course=course6, student_group=group1, faculty=fac5)
CourseAssignment.objects.create(course=course1, student_group=group2, faculty=fac1)
CourseAssignment.objects.create(course=course2, student_group=group2, faculty=fac2)
CourseAssignment.objects.create(course=course3, student_group=group2, faculty=fac3)
CourseAssignment.objects.create(course=course2, student_group=group3, faculty=fac2)
CourseAssignment.objects.create(course=course3, student_group=group3, faculty=fac3)
CourseAssignment.objects.create(course=course7, student_group=group3, faculty=fac1)
CourseAssignment.objects.create(course=course8, student_group=group4, faculty=fac2)
CourseAssignment.objects.create(course=course7, student_group=group4, faculty=fac1)
CourseAssignment.objects.create(course=course4, student_group=group5, faculty=fac4)
CourseAssignment.objects.create(course=course5, student_group=group6, faculty=fac4)
CourseAssignment.objects.create(course=course6, student_group=group7, faculty=fac5)
print("Course assignments created")

print("\n✅ Sample data added successfully!")
print(f"- {Department.objects.count()} Departments")
print(f"- {Faculty.objects.count()} Faculty")
print(f"- {Classroom.objects.count()} Classrooms")
print(f"- {Course.objects.count()} Courses")
print(f"- {TimeSlot.objects.count()} Time Slots")
print(f"- {StudentGroup.objects.count()} Student Groups")
print(f"- {CourseAssignment.objects.count()} Course Assignments")
