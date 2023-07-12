from django.contrib import admin

from socialapp.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','date_posted','title','content']


admin.site.register(Post,PostAdmin)
