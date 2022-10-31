from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from actors.serializers import *
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from .permissions import * 
# Create your views here.


class ActorsViewSet(viewsets.ModelViewSet):
	queryset = Actor.objects.all()
	serializer_class = ActorAPISerializer

	# Для редактирования необходимо авторизоваться:
	permission_classes = (IsAdminOrReadOnly, )

	


	@action(methods=['get'], detail=False)
	def country(self, request):
		
		""" Определяет путь /api/actors/country/ """

		c = Country.objects.all()
		return Response({'countries': [country.title for country in c]})



# Другая реализация:

# class ActorAPIView(generics.ListCreateAPIView):
# 	queryset = Actor.objects.all()
# 	serializer_class = ActorAPISerializer

# class ActorAPIUpdate(generics.RetrieveUpdateAPIView):
# 	queryset = Actor.objects.all()
# 	serializer_class = ActorAPISerializer


