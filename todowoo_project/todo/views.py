from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], request.POST['password1'])
        else:
            # Tell the user passwords didn't match
            print("Well, fella, the passwords don't match")
