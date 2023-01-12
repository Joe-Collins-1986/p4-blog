from django.urls import path
from .views import (
    PostDetailView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentUpdateView,
    CommentDeleteView,
    LikeView,
    About,
    AboutUpdate,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('like/<int:pk>', LikeView.as_view(), name="like_post"),

    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name="comment-update"),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name="comment-delete"),

    path('about/', About.as_view(), name="blog-about"),
    path('about/<int:pk>/update/', AboutUpdate.as_view(), name="about-update"),


]
