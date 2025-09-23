from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

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
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        return reverse_lazy('home-page')

@login_required
def logout_view(request):
    return render(request, 'Seguranca/logout.html')

class actual_logout_view(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home-page')
