from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home page")


def about(request):
    return render(request, 'about.html')


def services(request):
    return HttpResponse("this is services page")


def contact(request):
    return HttpResponse("this is contact page")
