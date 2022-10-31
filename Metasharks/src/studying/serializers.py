from rest_framework import serializers
from .models import (
	Curator,
	Direction,
	Discipline,
	Group,
	Student )


# Сериализыторы для всех моделей

class CuratorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Curator
		fields = '__all__'


class DirectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Direction
		fields = '__all__'


class DisciplineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Discipline
		fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ['student_name', 'student_last_name', 'direction', 'discipline', 'curator', 'group']