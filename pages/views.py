from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required

from pages.forms import ContactModelForm
from pages.models import ContactModel

class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'

class ContactTemplateVIew(CreateView):
    template_name = 'pages/contact.html'
    form_class = ContactModelForm
    model = ContactModel
    success_url = "/contact"

    