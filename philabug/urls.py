from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Abug's Admin"
admin.site.site_title = "Abug"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',include('blog.urls')),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
