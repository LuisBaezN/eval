from django.contrib import admin
from . import models

class ShopAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Productos, ShopAdmin)