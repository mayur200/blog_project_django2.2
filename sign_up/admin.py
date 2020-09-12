from django.contrib import  admin

from django.contrib import  admin
from sign_up.models import Post
from django.contrib.auth.admin import UserAdmin


class PostAdmin(admin.ModelAdmin):
    list_display = ['post','author']
    search_field = ['author']



admin.site.register(Post, PostAdmin)

