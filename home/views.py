from django.shortcuts import render, redirect


def start_page(request):
    return render(request, 'home/start.html')
