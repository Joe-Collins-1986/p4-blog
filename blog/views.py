from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.contrib.auth.models import User
from django.views.generic import (
    View,
    ListView,
    # DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Comment, Box
from .forms import CommentForm

# THIS FUNCTION HAS BEEN REPLACED BY THE BELOW CLASS PostListView
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)

class LikeView(View):

    def post(self, request, pk):
        post = get_object_or_404(Post, id=request.POST.get('post_liked_id'))

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post-detail', args=[pk]))

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # This takes the place of the defaul which would be: <app>/<model>_<viewtype>.html - therefore(blog/post_list.html)
    context_object_name = 'posts' # would pass object if not changed to post. Then would need to reference object not post in the template (see PostDetailView class for example)
    ordering = ["-date_posted"]
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # This takes the place of the defaul which would be: <app>/<model>_<viewtype>.html - therefore(blog/post_list.html)
    context_object_name = 'posts' # would pass object if not changed to post. Then would need to reference object not post in the template (see PostDetailView class for example)
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(View): # Because i have not specified a template name this will default to: <app>/<model>_<viewtype>.html - therefore(blog/post_detail.html)
    def get(self, request, pk, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.all().order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, pk, *args, **kwargs):

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        comments = post.comments.all().order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )



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


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # create and update will default to <app>/<model>_<form>.html - same template as create
    model = Comment
    fields = ['title', 'body']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        comment = self.get_object()
        if self.request.user.username == comment.name:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # Because i have not specified a template name this will default to a form for: <app>/<model>_<confirm_delete>.html - therefore(blog/post_confirm_delete.html)
    model = Comment
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if self.request.user.username == comment.name:
            return True
        return False




# ABOUT - PRACITICE FOR MAIN PROJECT


class About(View):

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        boxes = Box.objects.filter(user=request.user.id)

        if boxes.filter(name="Box1").exists():
            box1 = get_object_or_404(boxes, name="Box1")
            box1_color = box1.color
        else:
            box1 = "temp"
            box1_color = "danger"
        
        if boxes.filter(name="Box2").exists():
            box2 = get_object_or_404(boxes, name="Box2")
            box2_color = box2.color
        else:
            box2 = "temp"
            box2_color = "danger"

        if boxes.filter(name="Box3").exists():
            box3 = get_object_or_404(boxes, name="Box3")
            box3_color = box3.color
        else:
            box3 = "temp"
            box3_color = "danger"

        if boxes.filter(name="Box4").exists():
            box4 = get_object_or_404(boxes, name="Box4")
            box4_color = box4.color
        else:
            box4 = "temp"
            box4_color = "danger"


        return render(
                request,
                "blog/about.html",
                {
                    "box_1_color": box1_color,
                    "box_1": box1,

                    "box_2_color": box2_color,
                    "box_2": box2,

                    "box_3_color": box3_color,
                    "box_3": box3,

                    "box_4_color": box4_color,
                    "box_4": box4,

                    "user": user,
                    "admin1": "admin1"
                },
            )


    # def get(self, request):
    #     boxes = Box.objects.all()
    #     box1 = get_object_or_404(boxes, name="Box1")
    #     box2 = get_object_or_404(boxes, name="Box2")
    #     box3 = get_object_or_404(boxes, name="Box3")
    #     box4 = get_object_or_404(boxes, name="Box4")

    #     return render(
    #             request,
    #             "blog/about.html",
    #             {
    #                 "box_1": box1,
    #                 "box_2": box2,
    #                 "box_3": box3,
    #                 "box_4": box4,
    #             },
    #         )



# class AboutUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
class AboutUpdate(UpdateView): 
    model = Box
    template_name = 'blog/about_form.html'
    fields = ['visited',]

    def form_valid(self, form):
        if form.instance.visited:
            form.instance.color = "info"
        else:
            form.instance.color = "danger"
        form.instance.save()

        return HttpResponseRedirect(reverse('blog-about'))







    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    
    # def test_func(self):
    #     box = self.get_object()
    #     if self.request.user == box.name:
    #         return True
    #     return False
