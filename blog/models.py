from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80, default="none")
    title = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.title}"

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.post.id)])


class Box(models.Model):
    name = models.CharField(max_length=80)
    visited = models.BooleanField(default=False)
    color = models.CharField(max_length=80)

    def __str__(self):
        return f"Box Name: {self.name}"
    
    def get_absolute_url(self):
        return reverse('blog-about')