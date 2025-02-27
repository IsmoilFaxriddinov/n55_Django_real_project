import threading
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic import FormView, UpdateView

from users.forms import AccountForm, LoginForm, RegisterForm
from users.utils import send_email_confirmation

UserModel = get_user_model()

class LoginFormView(FormView):
    template_name = 'auth/user-login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        login(request=self.request, user=form.cleaned_data['user'])
        messages.success(self.request, 'Please, confirm your email or login')
    
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class RegisterView(FormView):
    template_name = 'auth/user-register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        email_thread = threading.Thread(target=send_email_confirmation, args=(user, self.request))
        email_thread.start()

        messages.success(self.request, 'Please, confirm your email or login')
    
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


def confirm_email(request, uid, token):
    try:
        user = UserModel.objects.get(id=uid)
    except UserModel.DoesNotExist:
        return redirect('users:login')
    
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your email address id verified')
        return redirect('/')
    else:
        messages.success(request, 'Link is not correnct')
        return redirect('/')
        

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'auth/user-acount.html'
    form_class = AccountForm
    success_url = reverse_lazy('users:account')
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

class UpdatePasswordView(FormView):
    template_name = 'auth/update-password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users:account')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        data = form.cleaned_data
        user = self.request.user
        user.set_password(raw_password=data['new_password1'])
        user.save()

        return super().form_valid(form)
    
    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
    
    
