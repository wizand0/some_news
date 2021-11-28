from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin

from polls.views import index, detail
from news import views


urlpatterns = [
    path('', index),
    path('polls/<int:question_id>', detail),
    path('admin/', admin.site.urls),
    path('blog/', views.blog_hendler),
    path('page/', views.page_hendler),
    path('about/', views.about_hendler),
    path('contact/', views.contact_hendler),
    path('index/', views.index_hendler),
    path('search/', views.search_hendler),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)