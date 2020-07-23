
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404, render
def get_list_of_questions(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, "get_list_of_questions.html",context)
    
def create_question(request):
    if request.method=="POST":
        new_question=Question()
        text,answer=request.POST.get('question'),request.POST.get('answer')
        if  text and answer:
            new_question.text=text
            new_question.answer=answer
            new_question.save()
            return render(request, "create_question_success.html")
        else:
            return render(request, "create_question_failure.html")
    else:
        return render(request, "create_question_form.html")

def get_question(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "each_question_form.html",{'question': question})
    
def update_question(request,question_id):
    modified_question = get_object_or_404(Question, pk=question_id)
    if request.method=="POST":
        text,answer=request.POST.get('question'),request.POST.get('answer')
        if  text and answer:
            modified_question.text=text
            modified_question.answer=answer
            modified_question.save()
            return render(request, "update_question_success.html")    
        else:
            return render(request, "update_question_failure.html")
    else:
        return render(request, "each_question_form.html",{'question': modified_question})
        
def delete_question(request,question_id):
    del_list=get_object_or_404(Question, pk=question_id)
    if del_list:
        del_list.delete()
        return render(request, "delete_question_success.html")
    else:
        return render(request, "delete_question_failure.html")

