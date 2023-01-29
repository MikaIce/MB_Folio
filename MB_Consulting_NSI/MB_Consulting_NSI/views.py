from django.shortcuts import render


def index(request):
    return render(request, "MB_Consulting_NSI/index.html")