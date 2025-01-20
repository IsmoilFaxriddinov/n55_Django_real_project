from django.urls import path

from blogs.views import BlogDetailView, BlogListView

app_name="blogs"

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='list'),
    path('blogs/<int:pk>', BlogDetailView.as_view(), name='detail')
]
