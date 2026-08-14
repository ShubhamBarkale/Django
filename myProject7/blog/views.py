from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post

def home(request):
    """Display all blog posts with filtering"""
    posts = Post.objects.all().order_by('-id')
    category = request.GET.get('category')
    
    if category:
        posts = posts.filter(catagory=category)
    
    categories = Post.objects.values_list('catagory', flat=True).distinct()
    
    context = {
        'posts': posts,
        'categories': categories,
        'selected_category': category
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, post_id):
    """Display a single post"""
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def create_post(request):
    """Create a new blog post"""
    if request.method == 'POST':
        title = request.POST.get('title')
        context = request.POST.get('context')
        category = request.POST.get('category')
        
        if title and context:
            Post.objects.create(
                title=title,
                context=context,
                catagory=category
            )
            messages.success(request, 'Post created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    return render(request, 'blog/create_post.html')

def delete_post(request, post_id):
    """Delete a blog post"""
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home')
    return render(request, 'blog/delete_post.html', {'post': post})

def edit_post(request, post_id):
    """Edit a blog post"""
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        post.title = request.POST.get('title', post.title)
        post.context = request.POST.get('context', post.context)
        post.catagory = request.POST.get('category', post.catagory)
        post.save()
        messages.success(request, 'Post updated successfully!')
        return redirect('post_detail', post_id=post.id)
    
    return render(request, 'blog/edit_post.html', {'post': post})
