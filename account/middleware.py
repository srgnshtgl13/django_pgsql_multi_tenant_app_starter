import django
from django.shortcuts import render,redirect


""" class LoginRequired(django.utils.deprecation.MiddlewareMixin):
    def process_exception(self, request, exception):
        if not request.user.is_authenticated:
            return redirect('account:login')
        return redirect('home') """



class LoginRequired:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response

    def process_exception(self,request, exception):
        if not request.user.is_authenticated:
            return redirect('account:login')
        return redirect('home')