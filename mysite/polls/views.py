from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.urls import reverse
from .models import Question,Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':
            latest_question_list,
               }
    return render(request, 'polls/index.html', context)
'''Функция render() принимает объект запроса в качестве первого аргумента, имя шаблона в качестве второго 
аргумента и словарь в качестве необязательного третьего аргумента. Она возвращает объект HttpResponse данного 
шаблона, отображенный в данном контексте.'''

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})
'''Функция get_object_or_404() принимает модель Django в качестве первого аргумента и произвольное 
количество ключевых аргументов, которое она передает в get() - функцию менеджера модели. Он вызывает 
Http404, если объект не существует.'''

def results(request, question_id):
    response = "You're looking at the results of question %s"
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', { 'question' : question })

def vote (request,question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        '''request.POST представляет собой объект, подобный словарю, который позволяет получить доступ 
        к отправленным данным по ключу. В этом случае request.POST ['choice'] возвращает идентификатор 
        выбранного варианта в виде строки. Значения request.POST всегда являются строками.'''
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question' : question,
                      'error_message' : "You didn't select a choice"})
        '''request.POST ['choice'] будет вызывать KeyError, если ключ choice не был предоставлен в POST. 
    Приведенный выше код проверяет KeyError и повторно отображает форму вопроса с сообщением об ошибке, 
    если choice не задано.'''
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''После увеличения счетчика выбора код возвращает HttpResponseRedirect, а не обычный HttpResponse. 
HttpResponseRedirect принимает один аргумент: URL-адрес, на который будет перенаправлен пользователь'''


# Create your views here.
