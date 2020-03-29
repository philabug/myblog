from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.home, name='home'),
    path('<slug:slug>',views.post, name='post'),
    path('about-me/',views.about_me, name='about-me')
]
