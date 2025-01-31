from django.shortcuts import render
from django.views.generic import FormView

from users.forms import RegisterForm

class RegisterView(FormView):
    template_name = 'auth/user-register.html'
    form_class = RegisterForm
    success_url = '/'
    
