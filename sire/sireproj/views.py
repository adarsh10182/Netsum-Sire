from django.shortcuts import render
from .models import Question
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'main.html')

def questions(request):
    q=Q()
    context={'p_qtn':None,'h_qtn':None,'hu_qtn':None}
    p_qtn=request.GET.get('check1',None)
    h_qtn=request.GET.get('check3',None)
    hu_qtn=request.GET.get('check2',None)
    chapter=request.GET.get('chapter','2')
    vessel=request.GET['vessel']
    query_args={ f'{vessel}__exact':True}
    if p_qtn:
        q = q & Q(PQtn="None")
        context['p_qtn']=True
    if h_qtn:
        q = q & Q(HQtn="None")
        context['h_qtn']=True
    if hu_qtn:
        q = q & Q(HuQtn="None")
        context['hu_qtn']=True
    if chapter:
        query_args['Chapter__exact']=chapter
    questions = (
        Question.objects
        .exclude(q)
        .filter(**query_args)
    )
    context['questions']=questions
    return render(request,'ques.html',context)