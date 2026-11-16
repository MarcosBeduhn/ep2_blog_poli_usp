from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author', 'post', 'posted_at')