from django.contrib import admin
from . models import postAdd

# Register your models here.
@admin.register(postAdd)
class adminNews(admin.ModelAdmin):
    list_display = ['name', 'seriya', 'image']