from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    UserPostListView,
)
from .import views

app_name = 'webapp'
urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.About, name="about"),
]