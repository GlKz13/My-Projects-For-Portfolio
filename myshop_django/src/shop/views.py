from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .forms import SearchForm
from django.contrib.postgres.search import SearchVector
# Create your views here.

def product_list(request):
	categories = Category.objects.all()
	products = Product.objects.all()
	search_form = SearchForm()
	context = {'products': products, 'search_form': search_form, 'categories': categories}
	return render(request, "shop/products/list.html", context)



def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug)
	cart_product_form = CartAddProductForm()
	context = {'product': product, 'cart_product_form': cart_product_form}
	return render(request, "shop/products/detail.html", context)



def product_list_by_category(request, category_slug):
	objects_by_category = Product.objects.filter(cat__slug=category_slug)
	print(objects_by_category)
	context = {'objects_by_category': objects_by_category}
	return render(request, "shop/products/show_category.html", context)

def product_search(request):
	search = request.GET.get('search')
	if search:
		results = None
		results = Product.objects.filter(name__search=search)
	else:
		results = ''
	print(results)
	context = {'results': results}
	return render(request, 'shop/products/search.html', context)



