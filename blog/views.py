from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, MoreContent
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator


def home(request):
    blog_list = Blog.objects.all().order_by('-id')
    
    page = request.GET.get('page', 1)
    
    paginator = Paginator(blog_list, 5)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    
    context = {
        'blogs': blogs,
        'post_title' : 'PhilTech Guru'
    }

    return render(request, 'blog/home.html', context)

def post(request, slug):
    blog_post = Blog.objects.filter(slug__iexact = slug)
    
    if blog_post.exists(): 
        blog_post = blog_post.first()
        more_contents = MoreContent.objects.filter(blog_id = blog_post.id)
    else: 
        return HttpResponse('<h1>Post Not Found</h1>')

    context = { 
        'post': blog_post,
        'post_title' : blog_post.title,
        'post_contents' : more_contents,
    } 
    return render(request, 'blog/post.html', context)
