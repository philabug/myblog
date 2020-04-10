import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Blog, MoreContent
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from hitcount.views import HitCountDetailView


def search_content(request):
    all_content = list(Blog.objects.all().values('id','title','category').order_by('-id'))
    return ({'all_content': json.dumps(all_content) } )

class BlogListView(ListView):
    model = Blog
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    paginate_by = 3
    queryset = Blog.objects.all().order_by('-id')

class BlogDetailView(HitCountDetailView):
    model = Blog
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_field = 'slug'
    count_hit = True
    
 
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['post_contents'] = MoreContent.objects.filter(blog_id = self.object.id)
        context.update({
        'popular_posts': Blog.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context

# def home(request):
#     blog_list = Blog.objects.all().order_by('-id')
    
#     page = request.GET.get('page', 1)
    
#     paginator = Paginator(blog_list, 5)
#     try:
#         blogs = paginator.page(page)
#     except PageNotAnInteger:
#         blogs = paginator.page(1)
#     except EmptyPage:
#         blogs = paginator.page(paginator.num_pages)
    
#     context = {
#         'blogs': blogs,
#         'post_title' : 'PhilTech Guru'
#     }

#     return render(request, 'blog/home.html', context)

# def post(request, slug):
#     blog_post = Blog.objects.filter(slug__iexact = slug)
#     count_hit = True
#     if blog_post.exists(): 
#         blog_post = blog_post.first()
#         more_contents = MoreContent.objects.filter(blog_id = blog_post.id)
#     else: 
#         return HttpResponse('<h1>Post Not Found</h1>')

#     context = { 
#         'post': blog_post,
#         'post_title' : blog_post.title,
#         'post_contents' : more_contents,
#     } 
#     return render(request, 'blog/post.html', context)

def about_me(request):
    context = {
        'post_title' : 'About Me'
    }
    return render(request, 'blog/aboutme.html', context)