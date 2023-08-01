from django.contrib import admin
from women.models import Woman, Category


class WomanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'photo', 'is_published', 'time_created', 'time_updated', 'cat')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', 'content', 'cat')
    list_filter = ('is_published', 'time_created')
    search_fields = ('title', 'content')


admin.site.register(Woman, WomanAdmin)
admin.site.register(Category)
