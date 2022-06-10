from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', "status")
    list_filter = ('publish', "author", "status")
    search_fields = ("title", "body")
    prepopulated_fields = {'slug': ("title",)}
    raw_id_fields = ("author", )
    ordering = ("status", "publish")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', "updated")
    list_filter = ('name', "email", "active")
    search_fields = ("name", "body")
