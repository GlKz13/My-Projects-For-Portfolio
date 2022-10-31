from django.urls import path
from . views import *

app_name = 'space_objects'

urlpatterns = [
    path('', show_main_page, name='main'),
    path('<slug:cat_slug>/', category_page, name='category_page'),
    path('category/<slug:obj_slug>/', obj_content, name='obj_content'),


]
