from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# THIS FUNCTION HAS BEEN REPLACED BY THE BELOW CLASS PostListView
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # This takes the place of the defaul which would be: <app>/<model>_<viewtype>.html - therefore(blog/post_list.html)
    context_object_name = 'posts' # would pass object if not changed to post. Then would need to reference object not post in the template (see PostDetailView class for example)
    ordering = ["-date_posted"]


class PostDetailView(DetailView): # Because i have not specified a template name this will default to: <app>/<model>_<viewtype>.html - therefore(blog/post_detail.html)
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView): # create and update will default to <app>/<model>_<form>.html
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # create and update will default to <app>/<model>_<form>.html - same template as create
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # Because i have not specified a template name this will default to a form for: <app>/<model>_<confirm_delete>.html - therefore(blog/post_confirm_delete.html)
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})