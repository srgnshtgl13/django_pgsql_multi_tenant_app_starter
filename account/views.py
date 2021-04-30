from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect,HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import logout
from django.utils.translation import gettext
from client.models import Client
from account.models import MyUser
from .forms import LoginForm, RegisterForm

class LoginView(View):
	template_name = 'account/login.html'
	form = LoginForm

	def post(self, request, *args, **kwargs):
		username = request.POST['email']
		passwd = request.POST['password']
		user = authenticate(username=username, password=passwd)
		if user is not None:
			login(request, user)
			return redirect('home:home')
		messages.error(request, 'Credentials were not provided!')
		return render(request, self.template_name, {'form': self.form})

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {'form': self.form})

class RegisterView(View):
	template_name = 'account/register.html'
	form = RegisterForm

	def post(self, request, *args, **kwargs):
		name = request.POST['name']
		last_name = request.POST['last_name']
		username = request.POST['email']
		passwd = request.POST['password']
		if not name or not last_name or not username or not passwd:
			messages.error(request, 'All fields are required!')
			return render(request, self.template_name, {'form': self.form})
		
		user = authenticate(username=username, password=passwd)
		if user:
			messages.error(request, 'User with these credentials already exists!')
			return render(request, self.template_name, {'form': self.form})

		client = Client(tenant_name=name, paid_until="2022-05-16", on_trial=True)
		client.save()
		if client:
			user = MyUser(first_name=name, last_name=last_name, client=client, email=username)
			user.set_password(passwd)
			user.save()
			login(request, user)
			return redirect('home:home')
		
		messages.error(request, 'error!')
		client.delete()
		return render(request, self.template_name, {'form': self.form})

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {'form': self.form})

def logout_view(request):
    logout(request)
    return redirect('account:login')

