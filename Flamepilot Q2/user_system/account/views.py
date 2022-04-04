from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from .forms import ProfileForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard/')
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render (request,'signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'signup.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard/')
    elif request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
@login_required(login_url='/login/')
def home(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'profile': profile})


@login_required(login_url='/login/')
def editprofile(request):
    if request.method == "POST":
        print('working')
        # u_form = 
        p_form = UpdateProfileForm(request.POST, instance=request.user.profile)
        if p_form.is_valid():
            # custom_form = p_form.save(False)
            # custom_form.save()
            p_form.save()

    else:
        p_form = UpdateProfileForm(instance=request.user.profile)
        print("incorrect")
    return render(request, 'editprofile.html', {'Pform': p_form})