from .forms import RegisterForm
from django.shortcuts import render, redirect
# Create your views here.

def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("/home")
	else:
		form = RegisterForm()
	context = {"form": form}
	return render(request, "register/register.html", context)


