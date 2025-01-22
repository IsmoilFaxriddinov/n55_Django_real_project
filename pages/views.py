from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required

from pages.models import ContactModel

class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'

class ContactTemplateVIew(CreateView):
    template_name = 'pages/contact.html'
    form_class = ContactModelForm
    model = ContactModel

    # def form_valid(self, form):
    #     form
    #     return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     response = super().form_invalid(form)
    #     response
    