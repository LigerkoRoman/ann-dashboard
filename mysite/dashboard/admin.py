from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


from import_export.admin import ImportExportActionModelAdmin

class BookAdmin(ImportExportActionModelAdmin):
    pass
admin.site.register(Cola1, BookAdmin)
admin.site.register(ColaFridge, BookAdmin)
admin.site.register(ColaRedShelf, BookAdmin)
admin.site.register(Panorama, BookAdmin)
admin.site.register(ColaFridgeImage, BookAdmin)
