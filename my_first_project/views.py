from django.http import HttpResponse
def home(request):
    return HttpResponse("welcome to  django")

def about(request):
    return HttpResponse("hari")         