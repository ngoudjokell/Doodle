from lesTaches.models import Task
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def myhome(request):
    context={}
    return render(request, "lesTaches/home.html", context)

def task_listing(request):
    from django.template import Template, Context
    objects=Task.objects.all().order_by('due_date')
    template=Template('{% for elem in objects %}')
