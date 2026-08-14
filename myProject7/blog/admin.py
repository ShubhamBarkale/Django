from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'catagory', 'id')
    search_fields = ('title', 'catagory')
    list_filter = ('catagory',)
    
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'catagory')
        }),
        ('Content', {
            'fields': ('context',)
        }),
    )

admin.site.register(Post, PostAdmin)
