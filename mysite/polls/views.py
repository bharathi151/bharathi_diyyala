from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from .models import Question
import datetime
import uuid
#
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
"""
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
"""
"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template. render(context, request))
"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
    
def index1(request):
    return HttpResponse("hello world.")
# Create your views here.

def index2(request):
    return HttpResponse(str(datetime.datetime.now()))

def index3(request):
    return HttpResponse(str(uuid.uuid4()))

def index4(request):
    s="""
    <!DOCTYPE html>
    <html>
    <body>
    
    <h2>List 1</h2>
    <ul>
        <li>Team 1</li>
        <li>Team 2</li>
        <li>Team 3</li>
    </ul>
    </body>
    </html>
    
    """
    return HttpResponse(s)
"""
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
"""
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)