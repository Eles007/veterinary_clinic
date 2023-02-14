from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_functions_website.urls')),
]

urlpatterns += [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
