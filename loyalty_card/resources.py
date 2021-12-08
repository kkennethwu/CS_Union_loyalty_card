from import_export import resources
from .models import *

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
        field = ('id', 'student_id')
