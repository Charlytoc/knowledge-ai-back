from django.shortcuts import render

def view_homepage(request):
    return render(request, 'home.html')