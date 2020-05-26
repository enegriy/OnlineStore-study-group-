from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User


class LoginView(TemplateView):
    template_name = "template/registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


class ProfilePage(TemplateView):
    template_name = "template/registration/profile.html"


class RegisterView(TemplateView):
    template_name = "template/registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, self.template_name)


def index(request):
    return render(request, "index.html")
