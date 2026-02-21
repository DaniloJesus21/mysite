from django.contrib import admin
from .models import Post
# Register your models here.

class PostAmin(admin.ModelAdmin):
  list_display = ("title", "slug", "author", "created_at", "status")
  list_filter = ('status',)
  search_fields = ["title", "content"]
  prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAmin)