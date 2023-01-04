from django.shortcuts import render

posts = [
    {
        'author': 'Joe C',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '12 Aug 2022'
    },
    {
        'author': 'Lizzy C',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': '14 Aug 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})