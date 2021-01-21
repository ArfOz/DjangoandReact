from django.contrib import admin
import nested_admin
from .models import Category, Comment, Post, PostView, Like


class PostInline(nested_admin.NestedTabularInline):
    model = Post

class CategoryAdmin(nested_admin.NestedModelAdmin):
    model = Category
    inlines =[PostInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Like)

# Register your models here.
