from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegForm, UserUpdateForm, ProfileUpdateForm 

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to log in')
            return redirect('login')
    else:
        form = UserRegForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required
def profile(request):
    
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'users/profile.html', context)