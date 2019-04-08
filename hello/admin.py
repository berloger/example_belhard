from django.contrib import admin
from .models import Videos, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 13

class VideoAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Videos, VideoAdmin)
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    fields = ['comment_text']

admin.site.register(Comment, CommentAdmin)