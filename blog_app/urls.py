from django.urls import path
from .views import HomePageView, AboutPageView, BlogDetailView, BlogCreateView

urlpatterns=[
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("post/<int:pk>", BlogDetailView.as_view(), name='post_detail'),
    path("post/new", BlogCreateView.as_view(), name="post_new"),
]