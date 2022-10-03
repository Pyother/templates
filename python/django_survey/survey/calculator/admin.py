from django.contrib import admin
from .models import Candidate, System
from import_export.admin import ImportExportModelAdmin

admin.site.register(Candidate)

@admin.register(System)
class SystemAdmin(ImportExportModelAdmin):
    list_display = ('employer', 'substract', 'system', 'value', 'border_date', 'comment')
    
