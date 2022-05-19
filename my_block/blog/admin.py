from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', "status")
    list_filter = ('publish', "author", "status")
    search_fields = ("title", "body")
    prepopulated_fields = {'slug': ("title",)}
    raw_id_fields = ("author", )
    ordering = ("status", "publish")
