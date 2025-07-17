from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render


from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("pools/index.html")
    context = {"latest_question_list": latest_question_list}
    # output = ",".join([q.question_text for q in latest_question_list])
    # return HttpResponse(context, template)
    return HttpResponse(request, "pools/index.html", context)

def detail(request, question_id):
    return HttpResponse("You are looking at question %s."% question_id )

def results(request, question_id):
    response = "Your're looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

