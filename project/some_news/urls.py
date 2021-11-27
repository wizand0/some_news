from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin

from polls.views import index, detail, blog_hendler

urlpatterns = [
    path('', index),
    path('polls/<int:question_id>', detail),
    path('admin/', admin.site.urls),
    path('blog/', blog_hendler)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)