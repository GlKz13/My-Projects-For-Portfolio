from rest_framework import generics 
from .models import *
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response




# Опрделеяем класс для пагинации
class OrderPagination(PageNumberPagination): 
	page_size = 10





#Блок кода для возврата заказов
#######################################################
class AllItemList(generics.ListCreateAPIView): 
	serializer_class = OrderSerializer
	pagination_class = OrderPagination			

	def get_queryset(self):
		queryset = Order.objects.all().order_by('-quantity')  # Здесь сортировка по количеству машин
		carBrand = self.request.query_params.get('carBrand')
		#print(self.request.query_params)
		if carBrand is not None:											# Для возврата машин определённой марки 
			queryset = queryset.filter(carBrand__carBrandTitle=carBrand)	# ( параметры прописываются в request )

		return queryset
		
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = OrderCreateSerializer
	queryset = Order.objects.all()

# Это класс позволяет добавлять заказ
class ItemCreate(generics.ListCreateAPIView):
	serializer_class = OrderCreateSerializer
	queryset = Order.objects.all()
#######################################################





# Код для возврата и изменения моделей машин
#######################################################
class CarModelList(generics.ListCreateAPIView):
	serializer_class = CarModelSerializer
	queryset = CarModel.objects.all()

class CarModelDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = CarModelSerializer
	queryset = CarModel.objects.all()	 
#######################################################



###  Для создания марки авто
#################################
class CarBrandList(generics.ListCreateAPIView):
	serializer_class = CarBrandSerializer
	queryset = CarBrand.objects.all()
	
class CarBrandDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = CarBrandSerializer
	queryset = CarBrand.objects.all()
#################################




### Для создания цвета
#################################
class ColorList(generics.ListCreateAPIView):
	serializer_class = ColorSerializer
	queryset = Color.objects.all()


class ColorDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ColorSerializer
	queryset = Color.objects.all()


class CarPerColor(generics.ListCreateAPIView):
	serializer_class = CarPerColorSerializer
#################################




#################################
@api_view(['GET'])
def carsPerColor(request):

	""" Позволяет получить количество машин по цветам 
		Цвет: Кол-во машин
	"""

	color_objects = Color.objects.all()
	color_serializer = ColorSerializer(color_objects, many=True)
	
	for item in color_serializer.data:
		item.update({'cars': f'{ Order.objects.filter(color__title=list(item.items())[1][1] ).count() }'})
	

	return Response(color_serializer.data)
#################################
