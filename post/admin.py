from django.contrib import admin
from .models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'published_date']
    list_display_links = ['published_date']
    list_filter = ['published_date']
    search_fields = ['title', 'content']
    list_editable = ['title']



    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
