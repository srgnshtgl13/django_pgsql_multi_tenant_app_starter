from django.shortcuts import render,redirect
#from django.views.generic import FormView
from django.views import View
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect,HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import logout
from django.utils.translation import gettext

class LoginView(View):
	template_name = 'account/login.html'
	form = LoginForm

	def post(self, request, *args, **kwargs):
		username = request.POST['email']
		passwd = request.POST['password']
		user = authenticate(username=username, password=passwd)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Credentials were not provided!')
			return render(request, self.template_name)

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {'form': self.form})


def logout_view(request):
    logout(request)
    return redirect('account:login')