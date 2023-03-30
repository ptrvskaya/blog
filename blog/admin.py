from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'description', 'topic', 'slug']
    list_editable = ['topic'] 
    prepopulated_fields = {'slug': ('title', )}
    
