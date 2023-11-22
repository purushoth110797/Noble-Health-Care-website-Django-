from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from .forms import SignupForm, SigninForm


class SignupView(View):
    template_name = "signup.html"

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(
                "/Home/"
            )  # Replace with the name of your website's home page
        return render(request, self.template_name, {"form": form})


class SigninView(View):
    template_name = "signin.html"

    def get(self, request, *args, **kwargs):
        form = SigninForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = SigninForm(request.POST)

        if form.is_valid():
            # Get the username and password from the form
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log in the user
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect(
                    "/Home/"
                )  # Redirect to the home page or wherever you want
            else:
                # If authentication fails, display an error message
                messages.error(request, "Invalid username or password.")
        return render(request, self.template_name, {"form": form})
