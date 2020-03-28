from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from taggit.managers import TaggableManager
from django.db.models.signals import pre_save
from philabug.utils import unique_slug_generator

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    category = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='', max_length=255)
    tags = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True )
    last_modified = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField(null=True, blank=True)

    slug = models.SlugField(max_length=250, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

def pre_save_receiver(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 

pre_save.connect(pre_save_receiver, sender = Blog) 


class MoreContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    header = models.CharField(max_length=255, blank=True)
    images = models.ImageField(upload_to='', max_length=255, blank=True)
    content = RichTextField(null=True, blank=True)
    codes = RichTextField(null=True, blank=True, config_name='special')

    def __str__(self):
        return self.blog.title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comments = models.TextField()




