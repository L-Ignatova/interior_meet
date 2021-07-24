from django.contrib import admin

# Register your models here.
from interior_meet.designs.models import Design, Like


class DesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'likes_count', 'city', 'country', 'description', 'image')

    def likes_count(self, obj):
        return obj.like_set.count()


admin.site.register(Design, DesignAdmin)
admin.site.register(Like)