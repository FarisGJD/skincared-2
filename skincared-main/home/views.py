from django.shortcuts import render


def index(request):
    """ Returns Home Page """
    return render(request, 'home/index.html')
