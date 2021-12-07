from import_export import resources
from .models import *

class SheetResource(resources.ModelResource):
    class Meta:
        model = Sheet
        field = ('id', 'student_id')
        # field = ('id', 'name', 'student_id', 'grade', 'cellphone', 'email')