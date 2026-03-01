from django.contrib import admin
from .models import Category, Post, Adv

# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Adv)