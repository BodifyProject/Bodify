from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User    
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def auth(request):
    

    if (request.method == "POST"):
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username.isalnum():
            print("username")
            messages.error(request, "Username can only contain letters and numbers.")
            return redirect('auth/')
            
        # Handling UNIQUE Usernames and Emails
        elif User.objects.filter(username=username):
            print("username")
            messages.error(request, "Username already exist! Try another username.")
            return redirect('/auth/')
            
            
        elif User.objects.filter(email=email):  
            print("email")
            messages.error(request, "Email already exist! Try another Email.")
            return redirect('/auth/')
            
        # Handling exception in password
        elif password1!=password2:
            print("password")
            messages.error(request,"Enter correct password for confirmation.")
            return redirect('/auth/')
            
        else:
            # Adding the details of user into User Database Table
            myuser = User.objects.create_user(username=username, email=email, password=password1)

            myuser.first_name = firstname
            myuser.last_name = lastname

            myuser.save()

            messages.success(request,"Hello "+ firstname +", your account has been successfully created !!!")

            user=authenticate(username=username, password=password1)         
            #this will return a not none value is the user is authenticated otherwise it returns none if the user have entered the wrong credentials"""

            if user is not None:
                login(request, user)
                messages.success(request,"Logged in !")
                return redirect("/")
                # login(request, myuser)


    return render(request, 'signup.html')

def loginAuth(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username, password=password)         
        #this will return a not none value is the user is authenticate otherwise it returns none if the user have entered the wrong credentials"""

        
        if user is not None:
            login(request, user)
            messages.success(request,"Logged in !")
            myuser=User.objects.filter(username=username)
            # fname= myuser.first_name
            return redirect("/")
            

        else:
            messages.error(request, "Wrong Credentials")

    return render(request, 'login.html')

