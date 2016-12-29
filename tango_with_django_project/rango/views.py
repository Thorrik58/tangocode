from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!")

def about(request):
    print 'test'
    return HttpResponse("Rango says here is the about page.<br> <a href=/>About</a>")

