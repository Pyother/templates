from django.urls import path
from calculator.views import index, EditorView

urlpatterns = [
    path('', index, name='index'),
    path('editor/', EditorView.as_view(), name='editor')
]