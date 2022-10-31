from django.shortcuts import render, get_object_or_404, redirect
from .serializers import *
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.generics import CreateAPIView
from .tasks import export_xml


import xlwt
from .models import (
	Curator,
	Direction,
	Discipline,
	Group,
	Student )

class CuratorViewSet(viewsets.ModelViewSet):
	queryset = Curator.objects.all()
	serializer_class = CuratorSerializer

class DirectionViewSet(viewsets.ModelViewSet):
	queryset = Direction.objects.all()
	serializer_class = DirectionSerializer

class DisciplineViewSet(viewsets.ModelViewSet):
	queryset = Discipline.objects.all()
	serializer_class = DisciplineSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class StudentViewSet(viewsets.ModelViewSet):
	serializer_class = StudentSerializer
	queryset = Student.objects.all()

	

	def create(self, request, *args, **kwargs):

		"""  Переопределяем create чтобы определить количество человек в группе"""

		if Student.objects.filter(group__number=request.data['group']).count() == 20:
			return HttpResponse('Too many people')
		
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
      
		user = serializer.save()
		print(user)
	

		data = serializer.data

		return Response(data)
		


# Эта функция для celery, импортируем её в urls
def export_xml_file(request):

	export_xml.delay()
	return redirect('/')














