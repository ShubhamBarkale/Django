from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog_list(request):
    """Display all blog posts"""
    blogs = Blog.objects.all().order_by('-created_at')
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, pk):
    """Display a single blog post"""
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog_detail.html', context)
