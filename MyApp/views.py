from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse(f"<html lang=\"en\"><body>"
                        f"It is now {now}"
                        f"</body></html>")
    
def hello_world(request):
    template = loader.get_template('helloworld.html') 
    return HttpResponse(template.render({},request))

def main(request):
    template = loader.get_template('main.html') 
    return HttpResponse(template.render({},request))

def interest(request):
    template = loader.get_template('interest.html') 
    return HttpResponse(template.render({},request))

def friends(request):
    template = loader.get_template('friends.html') 
    return HttpResponse(template.render({},request))


def name(request):
    context = {
        'friendly': True,
        'skills' : [
            {'name':'HTML/CSS','color':'green'},
            {'name':'Frontend','color':'yellow'},
            {'name':'Backend','color':'green'},
            {'name':'Python','color':'red'}   
        ]
    }
    return render(request, 'name.html', context)

from django.shortcuts import render

def project(request):
    context = {
        'friendly': True,
        'projects' : [
            {
                'name': 'Сайт-портфоліо', 
                'description': 'Мій персональний сайт розроблений на Django з використанням CSS блоків.', 
                'year': 2023, 
                'status': 'Завершено'
            },
            {
                'name': 'Додаток для списку справ', 
                'description': 'Простий менеджер завдань з можливістю додавання та видалення записів.', 
                'year': 2024, 
                'status': 'В розробці'
            },
            {
                'name': 'Телеграм бот', 
                'description': 'Бот для автоматизації замовлень у кав’ярні з інтеграцією бази даних.', 
                'year': 2024, 
                'status': 'Тестування'
            },
        ]
    }
    return render(request, 'project.html', context)

def contacts(request):
    context = {
        'friendly': True,
        'contacts': [
            {'name': 'Facebook', 'link': 'https://facebook.com', 'type': 'Соцмережа'},
            {'name': 'Instagram', 'link': 'https://instagram.com', 'type': 'Соцмережа'},
            {'name': 'Telegram', 'link': 'https://t.me/yourusername', 'type': 'Месенджер'},
            {'name': 'MAX', 'link': 'https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D1%82%D0%B2%D0%BE', 'type': 'Месенджер'}   
        ]
    }
    return render(request, 'contacts.html', context)