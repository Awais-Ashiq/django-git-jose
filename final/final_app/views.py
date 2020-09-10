from django.shortcuts import render
from .forms import UserModalForm,ProfileInfoForm
from .models import UserModel,UserModal

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                profile = UserModal.objects.get_or_create(id=user.id)
                print(profile)
                return HttpResponseRedirect(reverse('index',))
            else:
                return HttpResponse('User is not active!')
        else:
            print('Someone tried to login failed!')
            print('Username {} password {} '.format(username.password))
            return HttpResponse('Invalid user Name or password')
    else:
        return render(request,'final_app/login.html',{})

def index(request):
    username= {'username':user}
    return render(request, 'final_app/index.html',context=username)



def user(request):
    registerd = False
    if request.method == 'POST':
        user_form = UserModalForm(data=request.POST)
        profile_form = ProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registerd = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserModalForm()
        profile_form = ProfileInfoForm()

    return render(request,'final_app/user.html',
                         {'registerd':registerd,
                         'user_form':user_form,
                         'profile_form':profile_form})

def contact(request):
    return render(request,'final_app/contacts.html')
