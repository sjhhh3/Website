from django.contrib import admin
from blog.models import Post, BlogComment, Apost
from note.models import Notepost
from board.models import Comment
from gallery.models import Photo, PhotoComment
from myprofile.models import Profilepost

admin.site.register(Post)
admin.site.register(Notepost)
admin.site.register(Apost)
admin.site.register(Profilepost)
admin.site.register(Comment)
admin.site.register(BlogComment)
admin.site.register(Photo)
admin.site.register(PhotoComment)
# Register your models here.
