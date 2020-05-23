from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.db import connection
from home.models import Test
from firmalar.models import Firma
from django.utils.translation import activate
# Create your views here.


# @login_required(login_url='/login/')
def index(request):
	t_objects = Test.objects.all()
	return render(request, 'home.html', {'ts':t_objects})


def test_post(request):
	""" cursor = connection.cursor()
	try:
		cursor.execute("SELECT schema_name FROM information_schema.schemata;")
	finally:
		cursor.close()
	row = cursor.fetchone() """
	return HttpResponse('post')
