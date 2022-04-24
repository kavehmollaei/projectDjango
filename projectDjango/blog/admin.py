from django.contrib import admin
from blog.models import Post



class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    # fields=('title',)
    list_display =('title','counter_view','status')


admin.site.register(Post,PostAdmin)





#  Register your models here.
