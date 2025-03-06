from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcom {username}, Your Account Has Been Created')
            return redirect('login')
    else:
        #form = UserCreationForm()
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')