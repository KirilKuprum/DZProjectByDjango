from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Lesson
from django.shortcuts import render, get_object_or_404
import datetime
# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse(f"<html lang=\"en\"><body>"
                        f"It is now {now}"
                        f"</body></html>")
    
def shedule(request, weekId=1):
    lessons_from_db = Lesson.objects.filter(week_id=weekId)
    
    day_query = request.GET.get('day', '').strip().capitalize()
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekly_schedule = {}
    
    if day_query in days:
        weekly_schedule[day_query] = lessons_from_db.filter(day_of_week=day_query)
    else:
        for day in days:
            weekly_schedule[day] = lessons_from_db.filter(day_of_week=day)
    
    context = {
        'weekId': weekId,
        'schedule': weekly_schedule
    }
    
    return render(request, 'shedule.html', context)

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    
    context = {
        'lesson': lesson
    }
    return render(request, 'lesson_detail.html', context)

def teachers_list(request):
    lessons = Lesson.objects.exclude(teacher__isnull=True).exclude(teacher__exact='')
    
    teachers_data = {}
    
    for lesson in lessons:
        teacher_name = lesson.teacher.strip()
        
        if teacher_name not in teachers_data:
            teachers_data[teacher_name] = {
                'subjects': set(), 
                'lessons_count': 0
            }
            
        teachers_data[teacher_name]['subjects'].add(lesson.name)
        teachers_data[teacher_name]['lessons_count'] += 1
        
    context = {
        'teachers_data': teachers_data
    }
    return render(request, 'teachers.html', context)