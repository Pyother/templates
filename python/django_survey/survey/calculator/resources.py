from pyexpat import model
from import_export import resources
from .models import Candidate, System

class SystemResource(resources.ModelResource):
    class Meta:
        model = System
        