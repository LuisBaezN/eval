from django.contrib import admin
from . import models

class ShopAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(models.Productos, ShopAdmin)