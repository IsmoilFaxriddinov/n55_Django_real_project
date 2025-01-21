from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'

class ContactTemplateVIew(TemplateView):
    template_name = 'pages/contact.html'