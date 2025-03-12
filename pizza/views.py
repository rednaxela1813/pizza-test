from django.http import HttpResponse

def coming_soon(request):
    return HttpResponse("<h1>The application is under construction</h1>")

####

