from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Lesson
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse(f"<html lang=\"en\"><body>It is now {now}</body></html>")
    
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
        'lesson': lesson,
        'friendly': True,
        'projects' : [
            {'id': 0, 'name': 'Сайт-портфоліо', 'description': 'Мій персональний сайт...', 'year': 2023, 'status': 'Завершено'},
            {'id': 1, 'name': 'Додаток для списку справ', 'description': 'Простий менеджер...', 'year': 2024, 'status': 'В розробці'},
            {'id': 2, 'name': 'Телеграм бот', 'description': 'Бот для автоматизації...', 'year': 2024, 'status': 'Тестування'},
        ]
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

def project_detail(request, project_id):
    projects = [
        {'name': 'Сайт-портфоліо', 'description': 'Мій персональний сайт розроблений на Django з використанням CSS блоків.', 'year': 2023, 'status': 'Завершено'},
        {'name': 'Додаток для списку справ', 'description': 'Простий менеджер завдань з можливістю додавання та видалення записів.', 'year': 2024, 'status': 'В розробці'},
        {'name': 'Телеграм бот', 'description': 'Бот для автоматизації замовлень у кав’ярні з інтеграцією бази даних.', 'year': 2024, 'status': 'Тестування'},
    ]
    context = {
        'project': projects[project_id]
    }
    return render(request, 'project_detail.html', context)

def contacts(request):
    context = {
        'info': 'Сторінка контактів'
    }
    return render(request, 'contacts.html', context)
    
def fibonacci(request, amount=10, numb=0):
    fibon_numbers=[]
    a, b = 0, 1
    for i in range(0, amount):
        fibon_numbers.append(a)
        a, b = b, a + b
    return render(request, 'fibonacci.html', {
        'amount': amount,
        'result': fibon_numbers,
        'numb': numb,
        'count': fibon_numbers[numb]
    })
    
def catalog(request, id=None):
    all_products = [
        {"id": 1, "name": "Бездротові Навушники", "description": "Навушники з шумозаглушенням...", "price": 2499},
        {"id": 2, "name": "Смарт-годинник", "description": "Водонепроникний годинник...", "price": 4199},
        {"id": 3, "name": "Механічна Клавіатура", "description": "Компактна клавіатура...", "price": 1850},
        {"id": 4, "name": "Ергономічна Мишка", "description": "Бездротова мишка...", "price": 1200}
    ]
    context = {
        'id': id,
        'products': all_products
    }
    return render(request, 'catalog.html', context)