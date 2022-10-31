"""


	В модуль вынесена функция export для скачивания xml файла




"""


import xlwt
from django.http import HttpResponse, FileResponse
from .models import *


def export(request):

	""" xml файл """

	### Создание листа Directions and Disciplines

	wb = xlwt.Workbook(encoding='utf-8')
	sheet1 = wb.add_sheet('Directions')
	directions = Direction.objects.all().values_list('direction_title')
	
	row_num = 0
	directions_disciplines = ['Directions', 'Disciplines']

	for col in range(len(directions_disciplines)):
		sheet1.write(row_num, col, directions_disciplines[col])

	for d in directions:
		row = []
		row.append(d[0])
		disciplines = Discipline.objects.filter(direction__direction_title=d[0]).values_list('discipline_title')
		for disc in disciplines:
			row.append(disc[0])
		row_num += 1
		for column in range(len(row)):
			sheet1.write(row_num, column, row[column])

		



	### Создание листа Students

	sheet2 = wb.add_sheet('Students', cell_overwrite_ok=True)
	colums = ['Name', 'Last Name', 'Gender']
	row_num = 0
	groups = Group.objects.all().values_list('number')

	for col_num in range(len(colums)):
		sheet2.write(row_num, col_num, colums[col_num])

	row_num += 2
	for g in groups:
		total = Student.objects.all().count()
		male = Student.objects.filter(gender='male').count()

		sheet2.write(row_num, 0, f'Group {g[0]}')
		sheet2.write(row_num, 1, f'{male} men')
		sheet2.write(row_num, 2, f'{total - male} women')
		row_num += 2
		rows = Student.objects.filter(group__number=g[0]).values_list('student_name', 'student_last_name', 'gender')
		for row in rows:
			row_num += 1
			for col_num in range(len(row)):
				sheet2.write(row_num + 1, col_num, row[col_num])
		

	### Создание листа Curators

	sheet3 = wb.add_sheet('Curators', cell_overwrite_ok=True)
	row_num = 0
	

	colums = ['Curator', 'Direction', 'Phone Number']
	for col_num in range(len(colums)):
		sheet3.write(row_num, col_num, colums[col_num])

	rows = Curator.objects.all().values_list('name', 'curator_direction', 'phone')
	for row in rows:
		row_num += 1
		for col_num in range(len(row)):
			sheet3.write(row_num, col_num, row[col_num]) 




	# Возвращает HttpResponse

	response = HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename="students.xls"'
	wb.save(response)
	return response









