from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

userModel = get_user_model()

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                form.add_error(None, "Invalid email or password.")

    context = {
        "form": form
    }

    return render(request, 'accounts/login.html', context)

def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False) # Save form data into variable
            user.set_password(form.cleaned_data['password']) # hash user password
            user.save()

            return redirect('login')


    context = {
        "form": form
    }
    return render(request, 'accounts/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')