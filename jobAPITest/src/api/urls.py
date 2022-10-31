from django.urls import path
from .views import  (
	AllItemList, ItemDetail, CarModelList, 
	CarBrandList, ColorList, CarModelDetail, 
	ItemCreate, CarBrandDetail, ColorDetail,

	carsPerColor)

app_name = 'api'

urlpatterns = [
		# Выводит весь список заказов
		path('items/', AllItemList.as_view() ),
		# Позволяет создавать новые заказы
		path('items/create/', ItemCreate.as_view() ),
		# 
		path('detail/<int:pk>/', ItemDetail.as_view() ),
		
		# Список цветов и добавление новых
		path('colors/', ColorList.as_view() ),
		path('colors/<int:pk>', ColorDetail.as_view() ),


		# Выводит весь список марок и позволяет добавлять новые
		path('carBrands/', CarBrandList.as_view() ),
		# Позволяет изменять марки по ключу
		path('carBrands/<int:pk>', CarBrandDetail.as_view() ),



		# Выводит весь список моделей и позволяет добавлять новые
		path('carModels/', CarModelList.as_view() ),
		# Позволяет изменять модель машины по ключу
		path('carModels/<int:pk>/', CarModelDetail.as_view() ),
		
		# Цвета и количество машин
		path('carsPerColor/', carsPerColor ),
		
]