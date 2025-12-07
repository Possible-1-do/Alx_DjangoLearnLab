from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        request.user.email = email
        request.user.save()

    return render(request, "blog/register.html", {"form": form})
    return render(request, "blog/login.html", {"error": "Invalid username or password"})
    return render(request, "blog/profile.html")

