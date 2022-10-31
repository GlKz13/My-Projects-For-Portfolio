from .export_func import export
from .celery import app
from django.http import request



@app.task
def export_xml():
	export(request)	