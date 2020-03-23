from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "philabug"
admin.site.site_title = "philabug"
admin.site.index_title = "Welcom to admin page"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
