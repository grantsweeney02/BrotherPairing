from django.contrib import admin

from .models import Pledge, Brother, Pairing
# Register your models here.
admin.site.register(Brother)
admin.site.register(Pledge)
admin.site.register(Pairing)
