from django.contrib import admin
from .models import Tag, Article


admin.site.register(Tag)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
