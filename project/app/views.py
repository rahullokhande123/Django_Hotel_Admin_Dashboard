from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method=="POST":
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        contact1=request.POST.get('contact')
        password1=request.POST.get('password')
        cpassword1=request.POST.get('cpassword')

        if password1==cpassword1:
            
        else:
            msg="Password Not Match"
            return render(request,'registration.html',{'msg':msg})

        print(name1,email1,contact1,password1)
    else:
        return render(request,'registration.html')
    
def login(request):
    return render(request,'login.html')