from django.contrib import admin

from .models import Article, Avatar, Category, Tag

# Register your models here.
# user name: admin
# pwd: drf-vue
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Avatar)
