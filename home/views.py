from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.utils.translation import activate
from django.contrib import messages
from django.shortcuts import render
from django.db import connection
from home.models import Article
# Create your views here.


# @login_required(login_url='/login/')
def index(request):	
	if request.method == 'POST':
		title = request.POST["title"]
		desc = request.POST["desc"]
		if not title or not desc:
			messages.error(request, 'Title and desc are required!')
			return render(request, 'home.html')
		Article.objects.create(title=title, desc=desc)
		messages.success(request, 'Success!')
		articles = Article.objects.all()
		context = {
			'articles': articles
		}
		return render(request, 'home.html', context)
	
	articles = Article.objects.all()
	context = {
		'articles': articles
	}
	return render(request, 'home.html', context)
