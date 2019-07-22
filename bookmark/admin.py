from django.contrib import admin

# Register your models here.
from .models import Bookmark

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title','url')

admin.site.register(Bookmark, BookmarkAdmin)