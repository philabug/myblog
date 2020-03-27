from django.contrib import admin
from .models import Blog, MoreContent
from .forms import BlogForm

class InlineContent(admin.StackedInline):
    model = MoreContent
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    inlines = [InlineContent]
    list_display = ('id','title','pub_date','author','category')
    list_display_links = ('id','title')
    list_filter = ('category','tags')
    search_fields = ('title',)
    fieldsets = (
        (None, {
            "fields": (
                'title',
                'category',
                'banner',
                'tags',
                'author',
                'content'
            ),
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.author.id:
            obj.author = request.user
        obj.save()

admin.site.register(Blog, BlogAdmin)