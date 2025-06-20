from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from tasks.models import Task

def home_view(request):
    # tasks = Task.objects.all()
    # task_list = list(tasks.values('id', 'title', 'description'))
    # return HttpResponse("Hello And Welcome To Task Mangement App!")
    return render(request, 'home.html')


def contact_view(request):
    return render(request, 'contact.html')