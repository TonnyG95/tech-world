from django.contrib import admin
from .models import Post, Category, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)