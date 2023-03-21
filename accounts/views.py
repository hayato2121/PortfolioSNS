from django.shortcuts import render, redirect,get_object_or_404
from allauth.account import views
from django.views import View

class LoginView(views.LoginView):
    template_name = 'account/login.html'

class SignupView(views.SignupView):
    template_name = 'account/signup.html'

class LogoutView(views.LogoutView):
    template_name = 'account/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')
    
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')
    






    



