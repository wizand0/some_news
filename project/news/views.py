from django.shortcuts import render


def blog_hendler(request):
    contex = {}
    return render(request, 'news/blog.html', contex)


def page_hendler(request):
    contex = {}
    return render(request, 'news/page.html', contex)


def contact_hendler(request):
    contex = {}
    return render(request, 'news/contact.html', contex)


def about_hendler(request):
    contex = {}
    return render(request, 'news/about.html', contex)


def index_hendler(request):
    contex = {}
    return render(request, 'news/index.html', contex)


def search_hendler(request):
    contex = {}
    return render(request, 'news/search.html', contex)