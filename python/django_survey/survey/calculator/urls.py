from django.urls import path
from calculator.views import index, EditorView
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('editor/', EditorView.as_view(), name='editor'),
    path('Import_csv/', Import_csv, name="Import_csv")
]