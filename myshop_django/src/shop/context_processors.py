from .models import *
from .forms import * 

def products_by_category(request):
	return {'categories' : Category.objects.all() }

def search_form(request):
	return {'search_form': SearchForm() }
