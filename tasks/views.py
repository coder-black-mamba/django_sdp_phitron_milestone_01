from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from .models import Task

def task_view(request):
    # task = Task.objects.first()
    return JsonResponse({'task 1': 'Hello'}) 
    # return render(request, 'task.html')
# home  view
def home_view(request):
    return HttpResponse("Hello And Welcome To Task Mangement App")
# contact view
def contact_view(request):
    return HttpResponse("Contact Us At abusayed@absyd.xyz")

def manager_dashboard_view(request):
    return render(request, 'dashboard/manager-dashboard.html')

def user_dashboard_view(request):
    return render(request, 'dashboard/user-dashboard.html')
