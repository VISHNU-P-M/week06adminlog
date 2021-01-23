from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import auth, User

# Create your views here.
def adminlogin(request):
    if request.session.has_key('password'):
        return redirect(adminhome)
    else:
        if request.method=='POST':
            admin_name=request.POST['admin_name']
            password=request.POST['password']
            print(admin_name)
            if admin_name=='admin' and password=='admin':
                request.session['password']=password
                return JsonResponse('true',safe=False)
            else:
                return JsonResponse('false',safe=False)

        else:
            return render(request,'adminlogin.html')

def adminhome(request):
    if request.session.has_key('password'):
        user=User.objects.all()
        return render(request,'adminhome.html',{'user':user})
    else:
        return redirect(adminlogin)

def edit(request,id):
    if request.session.has_key('password'):
        if request.method=='POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']
            user = User.objects.get(id=id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email=email
            user.save()
            return redirect(adminhome)
        else:
            user=User.objects.get(id=id)
            return render(request,'edit.html',{'user':user})
    else:
        return redirect(adminlogin)
    
def delete(request,id):
    if request.session.has_key('password'):
        user=User.objects.get(id=id)
        user.delete()
        return redirect(adminhome)
    else:
        return redirect(adminlogin)

def logout(request):
    if request.session.has_key('password'):
        request.session.flush()
        return redirect(adminlogin)
def adduser(request):
    if request.session.has_key('password'):
        if request.method=='POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']
            if User.objects.filter(username=username).exists():
                return JsonResponse('user',safe=False)
            elif User.objects.filter(email=email).exists():
                return JsonResponse('email',safe=False)
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email)
                user.save()
                return JsonResponse('true',safe=False)
        else:
            return render(request,'adduser.html')
    else:
        return redirect(adminlogin)
