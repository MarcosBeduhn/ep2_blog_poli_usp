from django.contrib import admin
from .models import Post, Comment, Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_at')
    filter_horizontal = ('categories',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author', 'post', 'posted_at')