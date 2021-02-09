from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'user/index.html')


def product(request):
    return render(request, 'user/product.html')


def packages(request):
    return render(request, 'user/packages.html')


def aboutUs(request):
    return render(request, 'user/aboutUs.html')


def gallary(request):
    return render(request, 'user/gallary.html')


def feedback(request):
    return render(request, 'user/feedback.html')


def loginPage(request):
    return render(request, 'user/login.html')


def registerPage(request):
    return render(request, 'user/register.html')
