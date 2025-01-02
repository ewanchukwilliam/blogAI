from django.contrib import admin

from core.models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'author', 'created_at', 'gold_star')
    list_filter = ('created_at', 'gold_star')
    search_fields = ('content',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
