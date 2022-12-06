from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    fk_name = 'post'
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'count_like', 'created_at', 'author']
    search_fields = ['title', 'author']
    list_editable = ['count_like']
    list_filter = ['title', 'count_like', 'created_at']
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

