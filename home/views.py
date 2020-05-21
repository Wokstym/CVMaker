from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from home.models import University, Address, UserData


def start_page(request):
    return render(request, 'home/start.html')


def cv_list(request):
    user_data = UserData.objects.get(user_id=request.user.id)
    context = {
        'cvs':user_data.current_cvs
    }
    return render(request, 'home/cv_list.html', context)


def view_cv(request, cv_number=0):
    user_data = UserData.objects.get(user_id=request.user.id)
    cv = user_data.current_cvs[cv_number]

    context = {
        "name": cv.name,
        "description":cv.description
    }
    return render(request, 'home/view_cv.html', context)

# def view_cv(PDFTemplateView, cv_number=0):
#     template_name = "hello.html"
# print(request.user.id)
# user_data = UserData.objects.get(user_id=request.user.id)
# cv = user_data.current_cvs[cv_number]
#
#
# context = {
#     "name": cv.name
# }
# return render(request, 'home/view_cv.html', context)
