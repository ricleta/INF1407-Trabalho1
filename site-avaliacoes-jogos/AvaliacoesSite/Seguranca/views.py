from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetCompleteView

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data.get('group')
            user.groups.add(group)
            return HttpResponseRedirect(reverse_lazy('home-page'))
    else:
        form = SignUpForm()
    return render(request, 'Seguranca/signup.html', {'form': form})

class login_view(LoginView):
    template_name = 'Seguranca/login.html'
    redirect_authenticated_user = True

@login_required
def logout_view(request):
    return render(request, 'Seguranca/logout.html')

class actual_logout_view(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home-page')

class ChangePasswordView(PasswordChangeView):
    template_name = 'Seguranca/change_password.html'
    success_url = reverse_lazy('password_change_done')

class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'Seguranca/password_change_done.html'
    success_url = reverse_lazy('home-page')

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'Seguranca/password_reset_complete.html'
    success_url = reverse_lazy('home-page')
