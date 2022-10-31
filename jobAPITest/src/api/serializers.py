from rest_framework import serializers
from .models import Order, Color, CarBrand, CarModel




class ColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Color
		fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = CarModel
		fields = ['carModelTitle']	



class CarBrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = CarBrand
		fields = ['carBrandTitle']	



class OrderSerializer(serializers.ModelSerializer):
	color 	 = ColorSerializer(read_only=True)
	carModel = CarModelSerializer(read_only=True)
	carBrand = CarBrandSerializer(read_only=True)


	class Meta:
		model = Order
		fields = ['quantity', 'carBrand', 'carModel', 'color', 'date']

class OrderCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ['quantity', 'carBrand', 'carModel', 'color', 'date']



#class CarPerColorSerializer(serializers.Serializer):
#	color = serializers.CharField(max_length=100)
#	cars = serializers.IntegerField(read_only=True)

