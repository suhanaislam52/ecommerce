from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


from .forms import CustomUserCreationForm
@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created successfully! You can now log in.')
            login(request, user)  # Optionally log the user in after registration
            return redirect('profile')  # Redirect to the profile or any other page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'userauths/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'userauths/login.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'userauths/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('/')
