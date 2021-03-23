from django.contrib import admin
from .models import Substation, Photo
# Register your models here.



class SubAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('view', 'number')}



admin.site.register(Substation, SubAdmin)
admin.site.register(Photo)
