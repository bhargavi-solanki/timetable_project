import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable_project.settings')
django.setup()

from timetable.models import Department, Faculty, Classroom, Course, TimeSlot, StudentGroup, CourseAssignment, TimetableEntry

print("Clearing existing data...")
TimetableEntry.objects.all().delete()
CourseAssignment.objects.all().delete()
TimeSlot.objects.all().delete()
Course.objects.all().delete()
StudentGroup.objects.all().delete()
Faculty.objects.all().delete()
Classroom.objects.all().delete()
Department.objects.all().delete()
print("All existing data cleared!")

print("\nAdding BCA sample data...")

# Department
bca_dept = Department.objects.create(name="Bachelor of Computer Applications", code="BCA")
print("BCA Department created")

# Faculty
fac1 = Faculty.objects.create(name="Prof. Rajesh Kumar", email="rajesh@bca.edu", phone="9876543210", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac2 = Faculty.objects.create(name="Prof. Priya Sharma", email="priya@bca.edu", phone="9876543211", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac3 = Faculty.objects.create(name="Prof. Amit Patel", email="amit@bca.edu", phone="9876543212", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac4 = Faculty.objects.create(name="Prof. Sneha Gupta", email="sneha@bca.edu", phone="9876543213", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac5 = Faculty.objects.create(name="Prof. Vikram Singh", email="vikram@bca.edu", phone="9876543214", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac6 = Faculty.objects.create(name="Prof. Neha Agarwal", email="neha@bca.edu", phone="9876543215", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac7 = Faculty.objects.create(name="Prof. Sanjay Verma", email="sanjay@bca.edu", phone="9876543216", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac8 = Faculty.objects.create(name="Prof. Kavita Joshi", email="kavita@bca.edu", phone="9876543217", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac9 = Faculty.objects.create(name="Prof. Ankit Sharma", email="ankit@bca.edu", phone="9876543218", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac10 = Faculty.objects.create(name="Prof. Pooja Mehta", email="pooja@bca.edu", phone="9876543219", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac11 = Faculty.objects.create(name="Prof. Rahul Verma", email="rahul@bca.edu", phone="9876543220", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac12 = Faculty.objects.create(name="Prof. Deepak Rao", email="deepak@bca.edu", phone="9876543221", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac13 = Faculty.objects.create(name="Prof. Meera Patel", email="meera@bca.edu", phone="9876543222", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac14 = Faculty.objects.create(name="Prof. Arun Kumar", email="arun@bca.edu", phone="9876543223", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac15 = Faculty.objects.create(name="Prof. Sunita Yadav", email="sunita@bca.edu", phone="9876543224", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac16 = Faculty.objects.create(name="Prof. Manish Tiwari", email="manish@bca.edu", phone="9876543225", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac17 = Faculty.objects.create(name="Prof. Rita Das", email="rita@bca.edu", phone="9876543226", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
fac18 = Faculty.objects.create(name="Prof. Chandan Bose", email="chandan@bca.edu", phone="9876543227", department=bca_dept, available_days=["monday","tuesday","wednesday","thursday","friday"])
print("Faculty created")

# Classrooms
Classroom.objects.create(name="Room 101", building="Block A", capacity=60, room_type="lecture")
Classroom.objects.create(name="Room 102", building="Block A", capacity=60, room_type="lecture")
Classroom.objects.create(name="Room 103", building="Block A", capacity=60, room_type="lecture")
Classroom.objects.create(name="Room 104", building="Block A", capacity=40, room_type="lecture")
Classroom.objects.create(name="Room 105", building="Block A", capacity=40, room_type="lecture")
Classroom.objects.create(name="Lab 201", building="Block B", capacity=30, room_type="computer_lab")
Classroom.objects.create(name="Lab 202", building="Block B", capacity=30, room_type="computer_lab")
Classroom.objects.create(name="Lab 203", building="Block B", capacity=30, room_type="computer_lab")
Classroom.objects.create(name="Lab 301", building="Block C", capacity=30, room_type="computer_lab")
print("Classrooms created")

# Semester 1 Courses - Theory
sem1_theory1 = Course.objects.create(name="Fundamentals of Computer", code="BCA101", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac1)
sem1_theory2 = Course.objects.create(name="Programming in C", code="BCA102", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac2)
sem1_theory3 = Course.objects.create(name="Mathematics (Discrete Maths)", code="BCA103", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac3)

# Semester 1 Courses - Practical
sem1_prac1 = Course.objects.create(name="C Programming Lab", code="BCA104", credit_hours=2, course_type="practical", department=bca_dept, assigned_faculty=fac2)
sem1_prac2 = Course.objects.create(name="Computer Fundamentals Lab", code="BCA105", credit_hours=2, course_type="practical", department=bca_dept, assigned_faculty=fac1)

# Semester 2 Courses - Theory
sem2_theory1 = Course.objects.create(name="Data Structures", code="BCA201", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac4)
sem2_theory2 = Course.objects.create(name="Digital Electronics", code="BCA202", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac5)
sem2_theory3 = Course.objects.create(name="Mathematics II (Statistics)", code="BCA203", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac3)

# Semester 2 Courses - Practical
sem2_prac1 = Course.objects.create(name="Data Structures Lab", code="BCA204", credit_hours=2, course_type="practical", department=bca_dept, assigned_faculty=fac4)
sem2_prac2 = Course.objects.create(name="Digital Electronics Lab", code="BCA205", credit_hours=2, course_type="practical", department=bca_dept, assigned_faculty=fac5)

# Semester 3 Courses - Theory
sem3_theory1 = Course.objects.create(name="Object-Oriented Programming (C++)", code="BCA301", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac6)
sem3_theory2 = Course.objects.create(name="Database Management System", code="BCA302", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac7)
sem3_theory3 = Course.objects.create(name="Computer Organization & Architecture", code="BCA303", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac5)

# Semester 3 Courses - Practical
sem3_prac1 = Course.objects.create(name="OOP Lab (C++)", code="BCA304", credit_hours=2, course_type="practical", department=bca_dept, assigned_faculty=fac6)
sem3_prac2 = Course.objects.create(name="DBMS Lab", code="BCA305", credit_hours=2, course_type="practical", department=bca_dept, assigned_faculty=fac7)

# Semester 4 Courses - Theory
sem4_theory1 = Course.objects.create(name="Operating System", code="BCA401", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac8)
sem4_theory2 = Course.objects.create(name="Software Engineering", code="BCA402", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac9)
sem4_theory3 = Course.objects.create(name="Computer Networks", code="BCA403", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac10)

# Semester 4 Courses - Practical
sem4_prac1 = Course.objects.create(name="Operating System Lab", code="BCA404", credit_hours=2, course_type="practical", department=bca_dept, assigned_faculty=fac8)
sem4_prac2 = Course.objects.create(name="Computer Networks Lab", code="BCA405", credit_hours=2, course_type="practical", department=bca_dept, assigned_faculty=fac10)

# Semester 5 Courses - Theory
sem5_theory1 = Course.objects.create(name="Web Development (HTML/CSS/JS)", code="BCA501", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac11)
sem5_theory2 = Course.objects.create(name="Java Programming", code="BCA502", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac12)
sem5_theory3 = Course.objects.create(name="Python Programming", code="BCA503", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac13)

# Semester 5 Courses - Practical
sem5_prac1 = Course.objects.create(name="Web Development Lab", code="BCA504", credit_hours=2, course_type="practical", department=bca_dept, assigned_faculty=fac11)
sem5_prac2 = Course.objects.create(name="Java/Python Lab", code="BCA505", credit_hours=2, course_type="practical", department=bca_dept, assigned_faculty=fac12)

# Semester 6 Courses - Theory
sem6_theory1 = Course.objects.create(name="Artificial Intelligence (AI)", code="BCA601", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac14)
sem6_theory2 = Course.objects.create(name="Machine Learning", code="BCA602", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac15)
sem6_theory3 = Course.objects.create(name="Cyber Security", code="BCA603", credit_hours=3, course_type="theory", department=bca_dept, assigned_faculty=fac16)

# Semester 6 Courses - Practical
sem6_prac1 = Course.objects.create(name="Major Project", code="BCA604", credit_hours=4, course_type="practical", department=bca_dept, assigned_faculty=fac14)
sem6_prac2 = Course.objects.create(name="AI/ML Lab", code="BCA605", credit_hours=2, course_type="practical", department=bca_dept, assigned_faculty=fac15)

print("Courses created")

# Time Slots - Monday to Friday
days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
time_slots = [
    ("07:30", "08:30", "Lecture 1"),
    ("08:30", "09:30", "Lecture 2"),
    ("09:30", "10:00", "Break"),
    ("10:00", "11:00", "Lecture 3"),
    ("11:00", "12:00", "Lecture 4"),
    ("12:00", "13:00", "Lecture 5"),
    ("13:00", "13:15", "Short Break"),
    ("13:15", "14:15", "Lecture 6"),
]

for day in days:
    for start, end, slot_name in time_slots:
        is_break = slot_name == "Break" or slot_name == "Short Break"
        is_lunch = slot_name == "Short Break"
        TimeSlot.objects.create(day=day, start_time=start, end_time=end, is_break=is_break, is_lunch=is_lunch)
print("Time slots created")

# Student Groups
group1 = StudentGroup.objects.create(name="BCA Year 1 Sem 1", department=bca_dept, year=1, semester=1, semester_type="odd")
group2 = StudentGroup.objects.create(name="BCA Year 1 Sem 2", department=bca_dept, year=1, semester=2, semester_type="even")
group3 = StudentGroup.objects.create(name="BCA Year 2 Sem 3", department=bca_dept, year=2, semester=3, semester_type="odd")
group4 = StudentGroup.objects.create(name="BCA Year 2 Sem 4", department=bca_dept, year=2, semester=4, semester_type="even")
group5 = StudentGroup.objects.create(name="BCA Year 3 Sem 5", department=bca_dept, year=3, semester=5, semester_type="odd")
group6 = StudentGroup.objects.create(name="BCA Year 3 Sem 6", department=bca_dept, year=3, semester=6, semester_type="even")
print("Student groups created")

# Course Assignments - Semester 1
CourseAssignment.objects.create(course=sem1_theory1, student_group=group1, faculty=fac1)
CourseAssignment.objects.create(course=sem1_theory2, student_group=group1, faculty=fac2)
CourseAssignment.objects.create(course=sem1_theory3, student_group=group1, faculty=fac3)
CourseAssignment.objects.create(course=sem1_prac1, student_group=group1, faculty=fac2)
CourseAssignment.objects.create(course=sem1_prac2, student_group=group1, faculty=fac1)

# Course Assignments - Semester 2
CourseAssignment.objects.create(course=sem2_theory1, student_group=group2, faculty=fac4)
CourseAssignment.objects.create(course=sem2_theory2, student_group=group2, faculty=fac5)
CourseAssignment.objects.create(course=sem2_theory3, student_group=group2, faculty=fac3)
CourseAssignment.objects.create(course=sem2_prac1, student_group=group2, faculty=fac4)
CourseAssignment.objects.create(course=sem2_prac2, student_group=group2, faculty=fac5)

# Course Assignments - Semester 3
CourseAssignment.objects.create(course=sem3_theory1, student_group=group3, faculty=fac6)
CourseAssignment.objects.create(course=sem3_theory2, student_group=group3, faculty=fac7)
CourseAssignment.objects.create(course=sem3_theory3, student_group=group3, faculty=fac5)
CourseAssignment.objects.create(course=sem3_prac1, student_group=group3, faculty=fac6)
CourseAssignment.objects.create(course=sem3_prac2, student_group=group3, faculty=fac7)

# Course Assignments - Semester 4
CourseAssignment.objects.create(course=sem4_theory1, student_group=group4, faculty=fac8)
CourseAssignment.objects.create(course=sem4_theory2, student_group=group4, faculty=fac9)
CourseAssignment.objects.create(course=sem4_theory3, student_group=group4, faculty=fac10)
CourseAssignment.objects.create(course=sem4_prac1, student_group=group4, faculty=fac8)
CourseAssignment.objects.create(course=sem4_prac2, student_group=group4, faculty=fac10)

# Course Assignments - Semester 5
CourseAssignment.objects.create(course=sem5_theory1, student_group=group5, faculty=fac11)
CourseAssignment.objects.create(course=sem5_theory2, student_group=group5, faculty=fac12)
CourseAssignment.objects.create(course=sem5_theory3, student_group=group5, faculty=fac13)
CourseAssignment.objects.create(course=sem5_prac1, student_group=group5, faculty=fac11)
CourseAssignment.objects.create(course=sem5_prac2, student_group=group5, faculty=fac12)

# Course Assignments - Semester 6
CourseAssignment.objects.create(course=sem6_theory1, student_group=group6, faculty=fac14)
CourseAssignment.objects.create(course=sem6_theory2, student_group=group6, faculty=fac15)
CourseAssignment.objects.create(course=sem6_theory3, student_group=group6, faculty=fac16)
CourseAssignment.objects.create(course=sem6_prac1, student_group=group6, faculty=fac14)
CourseAssignment.objects.create(course=sem6_prac2, student_group=group6, faculty=fac15)

print("Course assignments created")

print("\n✅ BCA sample data added successfully!")
print(f"- {Department.objects.count()} Departments")
print(f"- {Faculty.objects.count()} Faculty")
print(f"- {Classroom.objects.count()} Classrooms")
print(f"- {Course.objects.count()} Courses")
print(f"- {TimeSlot.objects.count()} Time Slots")
print(f"- {StudentGroup.objects.count()} Student Groups")
print(f"- {CourseAssignment.objects.count()} Course Assignments")
