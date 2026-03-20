import random
from django.db import transaction
from .models import TimetableEntry, TimeSlot, CourseAssignment, Classroom

class TimetableGenerator:
    def __init__(self):
        self.timetable = []
        self.conflicts = []
        
    def generate(self):
        with transaction.atomic():
            TimetableEntry.objects.all().delete()
            
            assignments = list(CourseAssignment.objects.all().select_related(
                'course', 'student_group', 'faculty'
            ))
            
            if not assignments:
                return {'success': False, 'message': 'No course assignments found.'}
            
            time_slots = list(TimeSlot.objects.filter(is_break=False, is_lunch=False).order_by('day', 'start_time'))
            if not time_slots:
                return {'success': False, 'message': 'No time slots configured.'}
            
            classrooms = list(Classroom.objects.all())
            if not classrooms:
                return {'success': False, 'message': 'No classrooms configured.'}
            
            lecture_rooms = [r for r in classrooms if r.room_type == 'lecture']
            computer_labs = [r for r in classrooms if r.room_type == 'computer_lab']
            
            if not lecture_rooms:
                lecture_rooms = classrooms
            if not computer_labs:
                computer_labs = classrooms
            
            faculty_slot_used = {}
            room_slot_used = {}
            group_day_count = {}
            slot_room_used = {}
            
            random.shuffle(assignments)
            
            for assignment in assignments:
                course = assignment.course
                faculty = assignment.faculty
                student_group = assignment.student_group
                credit_hours = course.credit_hours
                
                assigned = 0
                attempts = 0
                max_attempts = 500
                
                while assigned < credit_hours and attempts < max_attempts:
                    attempts += 1
                    
                    random.shuffle(time_slots)
                    
                    for slot in time_slots:
                        day = slot.day
                        group_day_key = f"{student_group.id}_{day}"
                        current_count = group_day_count.get(group_day_key, 0)
                        
                        if current_count >= 5:
                            continue
                        
                        if course.course_type == 'theory':
                            courses_today = [e.course_assignment.course.id for e in self.timetable 
                                          if e.time_slot.day == day and 
                                          e.course_assignment.student_group.id == student_group.id]
                            if course.id in courses_today:
                                continue
                        
                        faculty_slot_key = f"{faculty.id}_{slot.id}"
                        if faculty_slot_key in faculty_slot_used:
                            continue
                        
                        available_rooms = computer_labs if course.course_type == 'practical' else lecture_rooms
                        random.shuffle(available_rooms)
                        
                        for room in available_rooms:
                            room_slot_key = f"{room.id}_{slot.id}"
                            if room_slot_key in room_slot_used:
                                continue
                            
                            entry = TimetableEntry.objects.create(
                                course_assignment=assignment,
                                classroom=room,
                                time_slot=slot
                            )
                            self.timetable.append(entry)
                            faculty_slot_used[faculty_slot_key] = True
                            room_slot_used[room_slot_key] = True
                            group_day_count[group_day_key] = current_count + 1
                            assigned += 1
                            break
                        
                        if assigned >= credit_hours:
                            break
                    
                if assigned < credit_hours:
                    self.conflicts.append(f"{course.name}: {assigned}/{credit_hours} hrs")
            
            self.fill_to_minimum(time_slots, faculty_slot_used, room_slot_used,
                               group_day_count, lecture_rooms, computer_labs)
            
            return {
                'success': True,
                'message': f'Timetable generated with {len(self.timetable)} entries.',
                'entries': len(self.timetable),
                'warnings': self.conflicts
            }
    
    def fill_to_minimum(self, time_slots, faculty_slot_used, room_slot_used,
                       group_day_count, lecture_rooms, computer_labs):
        all_assignments = list(CourseAssignment.objects.all().select_related(
            'course', 'student_group', 'faculty'
        ))
        
        groups = set(k.split('_')[0] for k in group_day_count.keys())
        
        for group_id in groups:
            for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
                group_day_key = f"{group_id}_{day}"
                current_count = group_day_count.get(group_day_key, 0)
                
                while current_count < 2:
                    day_slots = [s for s in time_slots if s.day == day]
                    if not day_slots:
                        break
                    
                    group_assignments = [a for a in all_assignments if str(a.student_group.id) == str(group_id)]
                    if not group_assignments:
                        break
                    
                    placed = False
                    for slot in day_slots:
                        for assignment in group_assignments:
                            faculty = assignment.faculty
                            course = assignment.course
                            
                            courses_today = [e.course_assignment.course.id for e in self.timetable 
                                          if e.time_slot.day == day and 
                                          e.course_assignment.student_group.id == int(group_id)]
                            if course.id in courses_today:
                                continue
                            
                            available_rooms = computer_labs if course.course_type == 'practical' else lecture_rooms
                            
                            for room in available_rooms:
                                room_slot_key = f"{room.id}_{slot.id}"
                                if room_slot_key in room_slot_used:
                                    continue
                                
                                entry = TimetableEntry.objects.create(
                                    course_assignment=assignment,
                                    classroom=room,
                                    time_slot=slot
                                )
                                self.timetable.append(entry)
                                room_slot_used[room_slot_key] = True
                                group_day_count[group_day_key] = current_count + 1
                                current_count += 1
                                placed = True
                                break
                            
                            if placed:
                                break
                        
                        if placed:
                            break
                    
                    if not placed:
                        break
