from django.contrib import admin
from blog.models import Post
from note.models import Notepost
from myprofile.models import Profilepost

admin.site.register(Post)
admin.site.register(Notepost)
admin.site.register(Profilepost)

# Register your models here.
