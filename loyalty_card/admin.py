from django.contrib import admin
from django.http.response import StreamingHttpResponse

# Register your models here.
from loyalty_card.models import *
from import_export.admin import ImportExportModelAdmin

from loyalty_card.resources import *


class User_Info_Admin(ImportExportModelAdmin):
    list_display = ('uid','name','pic_url','mtext','mdt')
admin.site.register(User_Info,User_Info_Admin)

class CCK_Admin(ImportExportModelAdmin):
    list_display = ('id', 'student_id', 'flg', 'getpoint')
    resource_class = CCKResource
admin.site.register(CCK,CCK_Admin)

class Sheet_Admin(ImportExportModelAdmin):
    list_display = ('id', 'student_id', 'getpoint')
    resource_class = SheetResource
admin.site.register(Sheet,Sheet_Admin)

class Github_Admin(ImportExportModelAdmin):
    list_display = ('id', 'student_id', 'getpoint')
    resource_class = GithubResource
admin.site.register(Github,Github_Admin)

class Hotpot_Admin(ImportExportModelAdmin):
    list_display = ('id', 'student_id', 'getpoint')
    resource_class = HotpotResource
admin.site.register(Hotpot,Hotpot_Admin)

class Machi_Admin(ImportExportModelAdmin):
    list_display = ('id', 'student_id', 'getpoint')
    resource_class = MachiResource
admin.site.register(Machi,Machi_Admin)

