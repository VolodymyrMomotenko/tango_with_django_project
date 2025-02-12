from django.contrib import admin
from rango.models import Category, Page

from rango.models import UserProfile

admin.site.register(UserProfile)

class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')

    
# Register your models here.
admin.site.register(Category, categoryAdmin)
admin.site.register(Page, PageAdmin)