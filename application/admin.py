from django.contrib import admin

# Register your models here.
from .models import Shop,ShopItem
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ShopResource(resources.ModelResource):
    class Meta:
        model = Shop
class ShopAdmin(ImportExportModelAdmin):
    resource_class = ShopResource

admin.site.register(Shop, ShopAdmin)
admin.site.register(ShopItem)