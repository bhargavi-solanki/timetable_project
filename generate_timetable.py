import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable_project.settings')
django.setup()

from timetable.generator import TimetableGenerator

generator = TimetableGenerator()
result = generator.generate()

print("Result:", result)
print("Entries created:", len(generator.timetable))
