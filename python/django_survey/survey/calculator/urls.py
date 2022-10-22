from django.urls import path
from calculator.views import index
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('output/', redirect_output, name='output')
]