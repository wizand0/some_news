from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Author, Category, Newsletter, Comment


class ArticleAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content', 'bio', 'comment')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Newsletter)
admin.site.register(Comment)
# Register your models here.
