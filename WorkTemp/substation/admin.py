from django.contrib import admin


from .models import Substation, City, View

admin.site.register(Substation)
admin.site.register(City)
admin.site.register(View)