from django.db import models

# Create your models here.





class Curator(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	curator_direction = models.ForeignKey('Direction', on_delete=models.CASCADE, null=True)
	phone = models.IntegerField()


	def __str__(self):
		return self.name






class Direction(models.Model):
	direction_title = models.CharField(max_length=150, null=True, blank=True)
	curator_name = models.OneToOneField(Curator, on_delete=models.CASCADE, null=True)


	def __str__(self):
		return self.direction_title




class Discipline(models.Model):
	
	discipline_title = models.CharField(max_length=150, null=True, blank=True)
	direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='disciplines')


	def __str__(self):
		return self.discipline_title






class Group(models.Model):
	number = models.IntegerField(unique=True)


	def __str__(self):
		return str(self.number)






class Student(models.Model):
	direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True)
	discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, null=True)
	curator = models.ForeignKey(Curator, on_delete=models.CASCADE, related_name='students', null=True)
	group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
	student_name = models.CharField(max_length=50, null=True )
	student_last_name = models.CharField(max_length=50, null=True)
	gender = models.CharField(max_length=10, null=True)
	

	def __str__(self):
		return self.student_name + ' ' + self.student_last_name










