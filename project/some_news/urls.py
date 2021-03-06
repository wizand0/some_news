from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

from news import views


urlpatterns = [
    path('', views.index_hendler),
    path('admin/', admin.site.urls),
    path('blog/', views.blog_hendler),
    path('page/', views.page_hendler),
    path('about/', views.about_hendler),
    path('contact/', views.contact_hendler),
    path('search/', views.search_hendler),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
