from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect(userhome)
    else:
        if request.method == 'POST':
            uname = request.POST['user_name']
            pswd = request.POST['password']
            user = auth.authenticate(username=uname,password=pswd)
            if user is not None:
                auth.login(request,user)
                return JsonResponse('true',safe=False)
            else :
                return JsonResponse('false',safe=False)
        else :
            return render(request,'userlogin.html')


def userhome(request):
    if request.user.is_authenticated:
        return render(request,'userhome.html')
    else:
        return redirect(login)

def signup(request):
    if request.user.is_authenticated:
        return redirect(userhome)
    else:
        if request.method=='POST':
            first_name=request.POST['first_name']
            second_name=request.POST['second_name']
            user_name=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            
            if User.objects.filter(username=user_name).exists():
                return JsonResponse('user',safe=False)
            elif User.objects.filter(email=email).exists():
                return JsonResponse('email',safe=False)
            else:
                user = User.objects.create_user(first_name=first_name,last_name=second_name,username=user_name,email=email,password=password)
                user.save()
                return JsonResponse('true',safe=False)
        else:
            return render(request,'usersignup.html')

    

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(login)

    
