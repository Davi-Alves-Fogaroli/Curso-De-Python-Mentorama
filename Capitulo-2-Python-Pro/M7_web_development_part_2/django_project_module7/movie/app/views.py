from django.shortcuts import render, HttpResponse

# Create your views here.

def filmes(request):
    return render(request, "app/home.html")