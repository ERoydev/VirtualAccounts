from django.shortcuts import render, redirect
from .forms import RegisterForm

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
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