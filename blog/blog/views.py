from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. i m a student")