from rest_framework import serializers
from .models import *


class ActorAPISerializer(serializers.ModelSerializer):

	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = Actor 
		fields = ['name', 'last_name', 'age', 'country', 'user']

