from django.shortcuts import render
from django.views.generic import FormView, CreateView

from users.forms import RegisterForm

class RegisterView(CreateView):
    template_name = 'auth/user-register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    