from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def home(request):
    users = Profile.objects.all()
    return render(request, 'home/home.html', {'users': users})

def profile(request):
    print (request.method)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print ("Else statement")
    else:
        form = ProfileForm()
    return render(request, 'home/profile.html', {'form' : form})
