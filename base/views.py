from django.shortcuts import render


POSTS = [
    {
        "author": "Anika",
        "title": "Post #1",
        "content": "First Post CONTENT",
        "date_posted": "June 8, 2020",
    },
    {
        "author": "Banika",
        "title": "Post #2",
        "content": "Second Post CONTENT",
        "date_posted": "June 11, 2020",
    },
]


def home(request):
    return render(request, "base/home.html")


def about(request):
    content = {"posts": POSTS}
    return render(request, "base/about.html", content)


def contact(request):
    return render(request, "base/contact.html")


def login(request):
    return render(request, "base/login.html")


def blog(request):
    return render(request, "blog/all_blogs.html")
