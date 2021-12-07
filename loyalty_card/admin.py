from django.contrib import admin
from django.http.response import StreamingHttpResponse

# Register your models here.
from loyalty_card.models import *
from import_export.admin import ImportExportModelAdmin

from loyalty_card.resources import SheetResource


class User_Info_Admin(ImportExportModelAdmin):
    list_display = ('uid','name','pic_url','mtext','mdt')
admin.site.register(User_Info,User_Info_Admin)


class Sheet_Admin(ImportExportModelAdmin):
    resource_class = SheetResource
    # list_display = ('name',
    # 'student_id',
    # 'grade',
    # 'cellphone',
    # 'email',
    # 'getpoint')
admin.site.register(Sheet,Sheet_Admin)