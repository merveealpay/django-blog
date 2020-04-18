from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


def home_view(request):
    if request.user.is_authenticated:
        context = {
            'name': 'merve',
        }
    else:
        context = {
            'name': 'Misafir',
        }
    return render(request,"home/home.html", context)
