from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from onesite.models import zone,foreign,monthcase,weekcase,info

# Register your models here.
@admin.register(zone)
class ZoneAdmin(ImportExportModelAdmin):
    list_display = ('code','city','count')

@admin.register(foreign)
class ForeignAdmin(ImportExportModelAdmin):
    list_display = ('country','count')

@admin.register(weekcase)
class WeekcaseAdmin(ImportExportModelAdmin):
    list_display = ('week','count')

@admin.register(monthcase)
class MonthcaseAdmin(ImportExportModelAdmin):
    list_display = ('month','count')

@admin.register(info)
class InfoAdmin(ImportExportModelAdmin):
    list_display = ('year','week','city',
    'gender','imported','age','count')