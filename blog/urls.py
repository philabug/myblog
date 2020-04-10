from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView

app_name = 'blog'
urlpatterns = [
    path('', BlogListView.as_view(), name='posts'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='detail'),
    # path('',views.home, name='home'),
    # path('<slug:slug>',views.post, name='post'),
    path('about-me/',views.about_me, name='about-me')
]
