from django.urls import path
from pages.views import HomeTemplateView, ContactTemplateVIew, AboutTemplateView

app_name = 'pages'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contact/', ContactTemplateVIew.as_view(), name='contact'),
    path("about/", AboutTemplateView.as_view(), name="about")
]
