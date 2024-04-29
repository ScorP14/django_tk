from django.contrib import admin

from .models import Substation

admin.site.register(Substation)



# prepopulated_fields = {"slug": ("name", )}