# Automated Timetable Generator - Specification

## 1. Project Overview

- **Project Name**: Automated Timetable Generator (ATSG)
- **Type**: Web Application (Django Backend + HTML/CSS/JS Frontend)
- **Core Functionality**: Intelligent timetable generation system that automatically creates conflict-free schedules considering faculty availability, course requirements, classrooms, and scheduling constraints
- **Target Users**: Educational institution administrators, academic coordinators, department heads

## 2. Technology Stack

- **Backend**: Python, Django 4.x
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript (Vanilla)
- **Database**: MySQL
- **Algorithm**: Constraint-based scheduling algorithm

## 3. Functionality Specification

### 3.1 Core Features

#### User Management
- Admin login/logout
- Dashboard with statistics

#### Data Management
- **Faculty Management**: Add, edit, delete faculty members with availability
- **Course Management**: Add, edit, delete courses with credit hours and department
- **Classroom Management**: Add, edit, delete classrooms with capacity
- **Department Management**: Add, edit, delete departments
- **Time Slot Management**: Define available time slots for scheduling

#### Timetable Generation
- Automatic timetable generation based on constraints
- Constraint validation before generation:
  - No faculty conflict (same faculty can't be in two places at once)
  - No classroom conflict (same room can't host two classes at once)
  - No student group conflict
  - Respect faculty availability preferences
- Manual timetable editing
- Regenerate option

#### Timetable Views
- View timetable by faculty
- View timetable by classroom
- View timetable by department/year
- Weekly timetable display

### 3.2 Data Models

```
Department
- id, name, code

Faculty
- id, name, email, phone, department (FK), available_days (JSON)

Course
- id, name, code, credit_hours, department (FK), faculty_preference (FK)

Classroom
- id, name, building, capacity, room_type (lecture/lab)

TimeSlot
- id, day, start_time, end_time, is_break

StudentGroup
- id, name, department (FK), year, semester

TimetableEntry
- id, course (FK), faculty (FK), classroom (FK), time_slot (FK), student_group (FK), semester
```

### 3.3 User Interface

- **Login Page**: Admin authentication
- **Dashboard**: Overview statistics, quick actions
- **Data Entry Pages**: Forms for all entities
- **Timetable View Pages**: Table/grid based views
- **Generation Page**: Configure and trigger generation

## 4. Acceptance Criteria

1. Admin can add/edit/delete all entities (faculty, courses, rooms, etc.)
2. Timetable generation completes without conflicts
3. Generated timetable respects all constraints
4. View timetables by different criteria (faculty, room, department)
5. Manual editing of timetable entries works
6. Responsive Bootstrap-based UI
7. MySQL database properly configured
