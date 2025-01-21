from django.urls import path
from pages.views import HomeTemplateView, ContactTemplateVIew

app_name = 'pages'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contact/', ContactTemplateVIew.as_view(), name='contact')
]
