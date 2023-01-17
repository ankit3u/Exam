from django.shortcuts import HttpResponse, redirect, render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    prod=Product.objects.all()
    return render(request,'dashboard.html',{'prod':prod})
    

@login_required(login_url="login")
def add_product(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST['name']
            desc = request.POST['desc']
            price = request.POST['price']
            

            Product.objects.create(name=name,desc=desc,price=price)
         
            return redirect('dashboard')

        return render(request,'addproduct.html')       
    else:
        return HttpResponseRedirect('/login/')

@login_required(login_url="login")
def delete(request,id):
    if request.user.is_authenticated:
        pi = Product.objects.get(pk=id)
        pi.delete()
        return redirect('dashboard')
    else:
        return HttpResponseRedirect('/login/')
@login_required(login_url="login")
def update(request,id):
    if request.user.is_authenticated:

        a = Product.objects.get(id=id)
        if request.method == "POST":
            name = request.POST['name']
            desc = request.POST['decs']
            price = request.POST['price']
            
            a = Product(id=id,name=name,desc=desc,price=price)        
            a.save()

            return redirect('dashboard')

        return render(request,'dashboard.html',{'a':a})
    else:
        return HttpResponseRedirect('/login/')
