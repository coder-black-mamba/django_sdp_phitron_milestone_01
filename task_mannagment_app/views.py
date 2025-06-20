from django.http import HttpResponse, JsonResponse
# from tasks.models import Task

def home_view(request):
    # tasks = Task.objects.all()
    # task_list = list(tasks.values('id', 'title', 'description'))
    return HttpResponse("Hello And Welcome To Task Mangement App!")


def contact_view(request):
    return HttpResponse("Contact Us At <a href='https://www.absyd.xyz' style='color: red;'>abusayed@absyd.xyz</a>")