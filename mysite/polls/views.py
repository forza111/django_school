from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import Question


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
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question' : question})
'''представление вызывает исключение Http404, если вопрос с запрошенным идентификатором не существует.'''

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response %question_id )

def vote (request,question_id):
    return HttpResponse("You're voting on question %s" %question_id )


# Create your views here.
