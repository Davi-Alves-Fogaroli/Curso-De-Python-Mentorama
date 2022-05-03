from django.contrib import admin
from blog_app.models import Post_um
from blog_app.models import Language
from blog_app.models import Programmer


# Register your models here.
admin.site.register(Post_um)
admin.site.register(Language)
admin.site.register(Programmer)