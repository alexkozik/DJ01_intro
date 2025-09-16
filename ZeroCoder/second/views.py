from django.http import HttpResponse

# Create your views here.

def data_page(request):
    return HttpResponse("<h2>Это заготовка для страницы data в моем первом проекте на Django</h2>")

def test_page(request):
    return HttpResponse("<h2>Это заготовка для страницы test в моем первом проекте на Django</h2>")