from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponse


def register_view(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #data save databased
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect('login')
            #return HttpResponse("Yes registration done successfully")          
        
        else:
            username = form.cleaned_data.get("username")
            messages.warning(request,f'Account not created for {username}')
            return redirect('register')    
    else:
        form = UserRegisterForm()
        context = {
            "form" : form
        }
        return render(request, 'users/register.html', context)

def profile_view(request):
    return render(request,'users/profile.html')