from django.shortcuts import render, redirect
from django.contrib.auth import login

from home.models import UserData
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(form.cleaned_data['name'])
            user_data = UserData(user=user, name=form.cleaned_data['name'], surname=form.cleaned_data['surname'],
                                 current_cvs=[])
            user_data.save()
            login(request, user)
            return redirect('start')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
