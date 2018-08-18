from django.http import HttpResponse
from django.shortcuts import render, redirect

from core.forms import RegisterUserForm
from core.tasks import send_registration_email


def home(request):
    return HttpResponse('<h1>home</h1>')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # user = form.save()
            send_registration_email.delay(request.user)
            return redirect('/')
    else:
        form = RegisterUserForm()

    context = {'form': form}
    return render(request, 'core/registration.html', context)
