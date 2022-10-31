from django.contrib import admin
from django.urls import path, include
from studying.views import *
from rest_framework import routers

## Создаём роутеры

curator_router = routers.DefaultRouter()
curator_router.register(r'curators', CuratorViewSet)


direction_router = routers.DefaultRouter()
curator_router.register(r'direction', DirectionViewSet)

discipline_router = routers.DefaultRouter()
discipline_router.register(r'discipline', DisciplineViewSet)


group_router = routers.DefaultRouter()
group_router.register(r'group', GroupViewSet)

student_router = routers.DefaultRouter()
student_router.register(r'students', StudentViewSet, basename='students')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(curator_router.urls)), # curators/<int:pk>
    path('', include(direction_router.urls)),
    path('', include(discipline_router.urls)),
    path('', include(group_router.urls)),
    path('', include(student_router.urls)),

    #  Путь для экспотра xml
    path('export/', export_xml_file, name='export'),

    ]
 
