from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/index')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/../index')
        
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('login')

    else:
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        if password_1 == password_2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password = password_1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                auth.login(request,user)
                messages.info(request,'User Created')
                #return redirect('/')

        else:
            messages.info(request,'Password not matching ...')   
            return redirect('register')  
        return redirect('/index')       


    else:
        return render(request,'register.html')
        
    # registered = False
    # if request.method == 'POST':
    #     user_form = UserForm(data=request.POST)
    #     if user_form.is_valid():
    #         user = user_form.save()
    #         user.set_password(user.password)
    #         user.save()
    #         registered = True
    #         return redirect('/')  

    #     else:
    #         print(user_form.errors)
    #         return redirect('register')  
    # else:
    #     user_form = UserForm()
        
    # return render(request,'registration.html',
    #                       {'user_form':user_form,
    #                        'registered':registered})


# Create your views here.
