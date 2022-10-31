from django.urls import path
from .views import *

app_name = 'law_s'

urlpatterns = [
    path('', main, name='main'),
    path('jacob_handerson', jacob, name='jacob'),

]