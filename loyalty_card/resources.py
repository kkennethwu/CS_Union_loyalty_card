from import_export import resources
from .models import *

class CCKResource(resources.ModelResource):
    class Meta:
        model = CCK
        field = ('id', 'student_id', 'flg')

class SheetResource(resources.ModelResource):
    class Meta:
        model = Sheet
        field = ('id', 'student_id')

class GithubResource(resources.ModelResource):
    class Meta:
        model = Github
        field = ('id', 'student_id')

class MachiResource(resources.ModelResource):
    class Meta:
        model = Machi
        field = ('id', 'student_id')
class HotpotResource(resources.ModelResource):
    class Meta:
        model = Hotpot
        import_id_fields = ['student_id']

